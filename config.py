env_vars = {
  # Get From my.telegram.org
  "API_HASH": "0e4dcf39643e83c3c174a0d2370e5b4a",
  # Get From my.telegram.org
  "API_ID": "20478011",
  #Get For @BotFather
  "BOT_TOKEN": "7248959755:AAFjDhuxqoOIw0492tYbk7BCu4wpN9I-nCQ",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "bio_com1",
  # Force Subs Channel username without @
  "CHANNEL": "Anime_Sparta",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "Chapter {chap_num} {chap_name} @Anime_Sparta",
  # Put Thumb Link 
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
