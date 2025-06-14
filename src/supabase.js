import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://pkilnxcjifczwxlyzabt.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBraWxueGNqaWZjend4bHl6YWJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4NDI5OTcsImV4cCI6MjA2NTQxODk5N30.9QclMSfdGoXZXQeXrC13m16CtIzHqCg-f1js5KkTLNE';

export const supabase = createClient(supabaseUrl, supabaseKey);