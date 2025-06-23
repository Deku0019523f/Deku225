#!/bin/bash

Deku-VPS Lightweight Installer

Pour Ubuntu 20.04 - SSH/SSL + SlowDNS

Couleurs

vert="\e[92m" rouge="\e[91m" fin="\e[0m"

clear echo -e "${vert}=============================" echo -e "     INSTALL DEKU-VPS     " echo -e "=============================${fin}"

Mise à jour du système

echo -e "[+] Mise à jour..." apt update -y && apt upgrade -y

Installation de paquets essentiels

echo -e "[+] Installation des paquets..." apt install -y curl wget screen net-tools dnsutils unzip stunnel4 dropbear

Configuration Dropbear (port 443)

echo -e "[+] Configuration de Dropbear..." echo "/bin/false" >> /etc/shells sed -i 's/NO_START=1/NO_START=0/' /etc/default/dropbear sed -i 's/DROPBEAR_PORT=22/DROPBEAR_PORT=443/' /etc/default/dropbear sed -i 's/DROPBEAR_EXTRA_ARGS=/DROPBEAR_EXTRA_ARGS="-p 109 -p 143"/' /etc/default/dropbear systemctl enable dropbear && systemctl restart dropbear

Installation Stunnel (SSL port 443)

echo -e "[+] Configuration de stunnel..." cat > /etc/stunnel/stunnel.conf << EOF cert = /etc/stunnel/stunnel.pem client = no [ssh] accept = 443 connect = 127.0.0.1:22 EOF

openssl req -new -x509 -days 3650 -nodes -out /etc/stunnel/stunnel.pem -keyout /etc/stunnel/stunnel.pem 
-subj "/C=CI/ST=Abidjan/L=Abidjan/O=DekuVPN/OU=VPN/CN=deku" chmod 600 /etc/stunnel/stunnel.pem sed -i 's/ENABLED=0/ENABLED=1/' /etc/default/stunnel4 systemctl restart stunnel4

SlowDNS - simple config (client/server dans /etc/slowdns)

echo -e "[+] Installation de SlowDNS..." mkdir -p /etc/slowdns && cd /etc/slowdns wget -q https://raw.githubusercontent.com/Deku0019523f/Deku-scanner/main/slowdns/server.key wget -q https://raw.githubusercontent.com/Deku0019523f/Deku-scanner/main/slowdns/server.pub wget -q https://raw.githubusercontent.com/Deku0019523f/Deku-scanner/main/slowdns/sldns-server wget -q https://raw.githubusercontent.com/Deku0019523f/Deku-scanner/main/slowdns/sldns-client chmod +x sldns-server sldns-client

Création du menu principal

cat > /usr/bin/deku-vps << 'EOF' #!/bin/bash while true; do clear echo -e "\e[92m===== MENU DEKU-VPS =====\e[0m" echo "1) Ajouter utilisateur SSH" echo "2) Supprimer utilisateur SSH" echo "3) Voir utilisateurs actifs" echo "4) Statistiques VPS" echo "5) Redémarrer SlowDNS" echo "0) Quitter" echo -n "Choix : "; read choix

case $choix in 1) read -p "Nom utilisateur : " user read -p "Mot de passe : " pass read -p "Durée (en jours) : " jours useradd -e $(date -d "$jours days" +%Y-%m-%d) -s /bin/false -M $user echo "$user:$pass" | chpasswd echo -e "\nUtilisateur $user ajouté avec succès !" read -p "Appuyez sur Entrée...";; 2) read -p "Nom utilisateur à supprimer : " user userdel -f $user && echo "Supprimé." read -p "Appuyez sur Entrée...";; 3) echo "Utilisateurs connectés Dropbear/SSH :" who read -p "Appuyez sur Entrée...";; 4) echo "RAM :" free -h echo "\nUtilisation CPU :" top -b -n1 | grep "Cpu(s)" echo "\nConnexions actives :" netstat -tunlp | grep ESTABLISHED read -p "Appuyez sur Entrée...";; 5) pkill sldns-server /etc/slowdns/sldns-server -udp :5300 -privkey-file /etc/slowdns/server.key -dns 8.8.8.8 & echo "SlowDNS redémarré." read -p "Appuyez sur Entrée...";; 0) exit;; *) echo "Option invalide." sleep 1;; esac done EOF chmod +x /usr/bin/deku-vps

Lancer SlowDNS automatiquement au démarrage

cat > /etc/systemd/system/slowdns.service << EOF [Unit] Description=SlowDNS Server After=network.target

[Service] ExecStart=/etc/slowdns/sldns-server -udp :5300 -privkey-file /etc/slowdns/server.key -dns 8.8.8.8 Restart=always

[Install] WantedBy=multi-user.target EOF systemctl enable slowdns && systemctl start slowdns

Fin

clear echo -e "${vert}Installation terminée ! Lancez le menu avec : deku-vps${fin}"

  
