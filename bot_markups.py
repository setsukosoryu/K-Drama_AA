from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Start markup
start_markup = InlineKeyboardMarkup(row_width=2)

choose_button = InlineKeyboardButton(text="Начать подбор", callback_data="choose_button")
help_button = InlineKeyboardButton(text="Помощь", callback_data="help_button")

start_markup.add(choose_button, help_button)

# Genres markup
choose_genres_markup = InlineKeyboardMarkup(row_width=3)

drama_button = InlineKeyboardButton(text="Драма", callback_data="drama_button")
romance_button = InlineKeyboardButton(text="Романтика", callback_data="romance_button")
thriller_button = InlineKeyboardButton(text="Триллер", callback_data="thriller_button")
mystery_button = InlineKeyboardButton(text="Мистика", callback_data="mystery_button")
comedy_button = InlineKeyboardButton(text="Комедия", callback_data="comedy_button")
life_button = InlineKeyboardButton(text="Повседневность", callback_data="life_button")
action_button = InlineKeyboardButton(text="Боевик", callback_data="action_button")
melodrama_button = InlineKeyboardButton(text="Мелодрама", callback_data="melodrama_button")
historical_button = InlineKeyboardButton(text="Исторические", callback_data="historical_button")
fantasy_button = InlineKeyboardButton(text="Фэнтези", callback_data="fantasy_button")
crime_button = InlineKeyboardButton(text="Криминал", callback_data="crime_button")
psychological_button = InlineKeyboardButton(text="Психология", callback_data="psychological_button")
political_button = InlineKeyboardButton(text="Политика", callback_data="political_button")
law_button = InlineKeyboardButton(text="Закон", callback_data="law_button")
supernatural_button = InlineKeyboardButton(text="Сверхъествественное", callback_data="supernatural_button")
medical_button = InlineKeyboardButton(text="Медицина", callback_data="medical_button")
horror_button = InlineKeyboardButton(text="Ужасы", callback_data="horror_button")
sci_fi_button = InlineKeyboardButton(text="Научная фантастика", callback_data="sci_fi_button")
youth_button = InlineKeyboardButton(text="Молодость", callback_data="youth_button")
military_button = InlineKeyboardButton(text="Военные", callback_data="military_button")
sports_button = InlineKeyboardButton(text="Спорт", callback_data="sports_button")
business_button = InlineKeyboardButton(text="Бизнес", callback_data="business_button")
food_button = InlineKeyboardButton(text="Еда", callback_data="food_button")
next_button = InlineKeyboardButton(text="Далее", callback_data="next_button")

choose_genres_markup.add(drama_button, romance_button, thriller_button, mystery_button, comedy_button, life_button,
                     action_button, melodrama_button, historical_button, fantasy_button, crime_button,
                     psychological_button, political_button, law_button, supernatural_button, medical_button,
                     horror_button, sci_fi_button, youth_button, military_button, sports_button, business_button,
                     food_button, next_button)

# Done markup
done_markup = InlineKeyboardMarkup(row_width=1)

done_button = InlineKeyboardButton(text="Продолжить", callback_data="done_button")

done_markup.add(done_button)

# Finish markup
finish_markup = InlineKeyboardMarkup(row_width=1)

finish_button = InlineKeyboardButton(text="Завершить", callback_data="finish_button")

finish_markup.add(finish_button)
