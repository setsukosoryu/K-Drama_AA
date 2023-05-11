import bot_markups as mp
import bot_replies as rp
from aiogram import Bot, Dispatcher, executor, types

bot = Bot("5911327805:AAGBAcmjU9JMSpgR3ANOnpTDtpUSDIVgDJ8")
dp = Dispatcher(bot)

genres_list = []

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_photo(message.chat.id, photo=rp.start_image, caption=rp.start_message,
                         reply_markup=mp.start_markup)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.chat.id, text=rp.help_message)


@dp.message_handler(commands=['choose'])
async def choose(message: types.Message):
    genres_list.clear()
    await bot.send_photo(message.chat.id, photo=rp.choose_genres_image, caption=rp.choose_genres_message,
                         reply_markup=mp.choose_genres_markup)


@dp.callback_query_handler(lambda c: c.data == "help_button")
async def help_callback(message: types.Message):
    await bot.send_message(message.from_user.id, text=rp.help_message)


@dp.callback_query_handler(lambda c: c.data == "choose_button")
async def choose_callback(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=rp.choose_genres_image, caption=rp.choose_genres_message,
                         reply_markup=mp.choose_genres_markup)


@dp.callback_query_handler(text="drama_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Драма"')
    if len(genres_list) <= 4:
        genres_list.append("Drama")


@dp.callback_query_handler(text="romance_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Романтика"')
    if len(genres_list) <= 4:
        genres_list.append("Romance")


@dp.callback_query_handler(text="thriller_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Триллер"')
    if len(genres_list) <= 4:
        genres_list.append("Thriller")


@dp.callback_query_handler(text="mystery_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Мистика"')
    if len(genres_list) <= 4:
        genres_list.append("Mystery")


@dp.callback_query_handler(text="comedy_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Комедия"')
    if len(genres_list) <= 4:
        genres_list.append("Comedy")


@dp.callback_query_handler(text="life_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Повседневность"')
    if len(genres_list) <= 4:
        genres_list.append("Life")


@dp.callback_query_handler(text="action_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Боевик"')
    if len(genres_list) <= 4:
        genres_list.append("Action")


@dp.callback_query_handler(text="melodrama_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Мелодрама"')
    if len(genres_list) <= 4:
        genres_list.append("Melodrama")


@dp.callback_query_handler(text="historical_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Исторические"')
    if len(genres_list) <= 4:
        genres_list.append("Historical")


@dp.callback_query_handler(text="fantasy_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Фэнтези"')
    if len(genres_list) <= 4:
        genres_list.append("Fantasy")


@dp.callback_query_handler(text="crime_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Криминал"')
    if len(genres_list) <= 4:
        genres_list.append("Crime")


@dp.callback_query_handler(text="psychological_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Психология"')
    if len(genres_list) <= 4:
        genres_list.append("Psychological")


@dp.callback_query_handler(text="political_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Политика"')
    if len(genres_list) <= 4:
        genres_list.append("Political")


@dp.callback_query_handler(text="law_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Закон"')
    if len(genres_list) <= 4:
        genres_list.append("Law")


@dp.callback_query_handler(text="supernatural_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Сверхъестественное"')
    if len(genres_list) <= 4:
        genres_list.append("Supernatural")


@dp.callback_query_handler(text="medical_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Медицина"')
    if len(genres_list) <= 4:
        genres_list.append("Medical")


@dp.callback_query_handler(text="horror_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Ужасы"')
    if len(genres_list) <= 4:
        genres_list.append("Horror")


@dp.callback_query_handler(text="sci_fi_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Научная фантастика"')
    if len(genres_list) <= 4:
        genres_list.append("Sci-Fi")


@dp.callback_query_handler(text="youth_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Молодость"')
    if len(genres_list) <= 4:
        genres_list.append("Youth")


@dp.callback_query_handler(text="military_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Военные"')
    if len(genres_list) <= 4:
        genres_list.append("Military")


@dp.callback_query_handler(text="sports_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Спорт"')
    if len(genres_list) <= 4:
        genres_list.append("Sports")


@dp.callback_query_handler(text="business_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Бизнес"')
    if len(genres_list) <= 4:
        genres_list.append("Business")


@dp.callback_query_handler(text="food_button")
async def drama_callback(callback: types.CallbackQuery):
    await callback.answer('Вы выбрали жанр "Еда"')
    if len(genres_list) <= 4:
        genres_list.append("Food")


@dp.callback_query_handler(lambda c: c.data == "next_button")
async def next_callback(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=rp.done_image, caption=rp.done_message,
                         reply_markup=mp.done_markup)


@dp.callback_query_handler(lambda c: c.data == "done_button")
async def next_callback(message: types.Message):
    if sorted(genres_list) == sorted(rp.list_0):
        await bot.send_photo(message.from_user.id, photo=rp.move_to_heaven_image, caption=rp.move_to_heaven_message)
        await bot.send_photo(message.from_user.id, photo=rp.navillera_image, caption=rp.navillera_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_1):
        await bot.send_photo(message.from_user.id, photo=rp.weak_hero_class_image, caption=rp.weak_hero_class_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_2):
        await bot.send_photo(message.from_user.id, photo=rp.hospital_playlist_image, caption=rp.hospital_playlist_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_3):
        await bot.send_photo(message.from_user.id, photo=rp.flower_of_evil_image, caption=rp.flower_of_evil_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_4):
        await bot.send_photo(message.from_user.id, photo=rp.alchemy_of_souls_image, caption=rp.alchemy_of_souls_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_5):
        await bot.send_photo(message.from_user.id, photo=rp.reply_1988_image, caption=rp.reply_1988_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_6):
        await bot.send_photo(message.from_user.id, photo=rp.my_mister_image, caption=rp.my_mister_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_7):
        await bot.send_photo(message.from_user.id, photo=rp.the_glory_image, caption=rp.the_glory_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_8):
        await bot.send_photo(message.from_user.id, photo=rp.under_the_queens_umbrella_image, caption=rp.under_the_queens_umbrella_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_9):
        await bot.send_photo(message.from_user.id, photo=rp.prison_playbook_image, caption=rp.prison_playbook_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_10):
        await bot.send_photo(message.from_user.id, photo=rp.mr_queen_image, caption=rp.mr_queen_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_11):
        await bot.send_photo(message.from_user.id, photo=rp.mother_image, caption=rp.mother_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_12):
        await bot.send_photo(message.from_user.id, photo=rp.extraordinary_attorney_woo_image, caption=rp.extraordinary_attorney_woo_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_13):
        await bot.send_photo(message.from_user.id, photo=rp.crash_landing_on_you_image, caption=rp.crash_landing_on_you_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_14):
        await bot.send_photo(message.from_user.id, photo=rp.vincenzo_image, caption=rp.vincenzo_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_15):
        await bot.send_photo(message.from_user.id, photo=rp.its_okay_to_not_be_okay_image, caption=rp.its_okay_to_not_be_okay_message)
        await bot.send_photo(message.from_user.id, photo=rp.kill_me_heal_me_image, caption=rp.kill_me_heal_me_message)
        await bot.send_photo(message.from_user.id, photo=rp.its_okay_thats_love_image, caption=rp.its_okay_thats_love_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_16):
        await bot.send_photo(message.from_user.id, photo=rp.signal_image, caption=rp.signal_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_17):
        await bot.send_photo(message.from_user.id, photo=rp.kingdom_image, caption=rp.kingdom_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_18):
        await bot.send_photo(message.from_user.id, photo=rp.happiness_image, caption=rp.happiness_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_19):
        await bot.send_photo(message.from_user.id, photo=rp.mr_sunshine_image, caption=rp.mr_sunshine_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_20):
        await bot.send_photo(message.from_user.id, photo=rp.tomorrow_image, caption=rp.tomorrow_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_21):
        await bot.send_photo(message.from_user.id, photo=rp.healer_image, caption=rp.healer_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_22):
        await bot.send_photo(message.from_user.id, photo=rp.sky_castle_image, caption=rp.sky_castle_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_23):
        await bot.send_photo(message.from_user.id, photo=rp.the_red_sleeve_image, caption=rp.the_red_sleeve_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_24):
        await bot.send_photo(message.from_user.id, photo=rp.mouse_image, caption=rp.mouse_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_25):
        await bot.send_photo(message.from_user.id, photo=rp.stranger_image, caption=rp.stranger_message)
        await bot.send_photo(message.from_user.id, photo=rp.defendant_image, caption=rp.defendant_message)
        await bot.send_photo(message.from_user.id, photo=rp.big_mouth_image, caption=rp.big_mouth_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_26):
        await bot.send_photo(message.from_user.id, photo=rp.twenty_five_twenty_one_image, caption=rp.twenty_five_twenty_one_message)
        await bot.send_photo(message.from_user.id, photo=rp.our_blues_image, caption=rp.our_blues_message)
        await bot.send_photo(message.from_user.id, photo=rp.my_liberation_notes_image, caption=rp.my_liberation_notes_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_27):
        await bot.send_photo(message.from_user.id, photo=rp.the_uncanny_counter_image, caption=rp.the_uncanny_counter_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_28):
        await bot.send_photo(message.from_user.id, photo=rp.goblin_image, caption=rp.goblin_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_29):
        await bot.send_photo(message.from_user.id, photo=rp.dp_image, caption=rp.dp_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_30):
        await bot.send_photo(message.from_user.id, photo=rp.weightlifting_fairy_kim_bok_joo_image, caption=rp.weightlifting_fairy_kim_bok_joo_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_31):
        await bot.send_photo(message.from_user.id, photo=rp.taxi_driver_image, caption=rp.taxi_driver_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_32):
        await bot.send_photo(message.from_user.id, photo=rp.six_flying_dragons_image, caption=rp.six_flying_dragons_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_33):
        await bot.send_photo(message.from_user.id, photo=rp.youth_of_may_image, caption=rp.youth_of_may_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_34):
        await bot.send_photo(message.from_user.id, photo=rp.life_on_mars_image, caption=rp.life_on_mars_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_35):
        await bot.send_photo(message.from_user.id, photo=rp.the_devil_judge_image, caption=rp.the_devil_judge_message)
        await bot.send_photo(message.from_user.id, photo=rp.law_school_image, caption=rp.law_school_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_36):
        await bot.send_photo(message.from_user.id, photo=rp.racket_boys_image, caption=rp.racket_boys_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_37):
        await bot.send_photo(message.from_user.id, photo=rp.through_the_darkness_image, caption=rp.through_the_darkness_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_38):
        await bot.send_photo(message.from_user.id, photo=rp.beyond_evil_image, caption=rp.beyond_evil_message)
        await bot.send_photo(message.from_user.id, photo=rp.children_of_nobody_image, caption=rp.children_of_nobody_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_39):
        await bot.send_photo(message.from_user.id, photo=rp.missing_the_other_side_image, caption=rp.missing_the_other_side_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_40):
        await bot.send_photo(message.from_user.id, photo=rp.hometown_cha_cha_cha_image, caption=rp.hometown_cha_cha_cha_message)
        await bot.send_photo(message.from_user.id, photo=rp.live_image, caption=rp.live_message)
        await bot.send_photo(message.from_user.id, photo=rp.eulachacha_waikiki_image, caption=rp.eulachacha_waikiki_message)
        await bot.send_photo(message.from_user.id, photo=rp.once_again_image, caption=rp.once_again_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_41):
        await bot.send_photo(message.from_user.id, photo=rp.the_penthouse_war_in_life_image, caption=rp.the_penthouse_war_in_life_message)
        await bot.send_photo(message.from_user.id, photo=rp.the_king_of_pigs_image, caption=rp.the_king_of_pigs_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_42):
        await bot.send_photo(message.from_user.id, photo=rp.dear_my_friends_image, caption=rp.dear_my_friends_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_43):
        await bot.send_photo(message.from_user.id, photo=rp.arthdal_chronicles_image, caption=rp.arthdal_chronicles_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_44):
        await bot.send_photo(message.from_user.id, photo=rp.the_guest_image, caption=rp.the_guest_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_45):
        await bot.send_photo(message.from_user.id, photo=rp.dr_romantic_image, caption=rp.dr_romantic_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_46):
        await bot.send_photo(message.from_user.id, photo=rp.while_you_were_sleeping_image, caption=rp.while_you_were_sleeping_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_47):
        await bot.send_photo(message.from_user.id, photo=rp.our_beloved_summer_image, caption=rp.our_beloved_summer_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_48):
        await bot.send_photo(message.from_user.id, photo=rp.sweet_home_image, caption=rp.sweet_home_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_49):
        await bot.send_photo(message.from_user.id, photo=rp.eighteen_again_image, caption=rp.eighteen_again_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_50):
        await bot.send_photo(message.from_user.id, photo=rp.moon_lovers_scarlet_heart_ryeo_image, caption=rp.moon_lovers_scarlet_heart_ryeo_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_51):
        await bot.send_photo(message.from_user.id, photo=rp.partners_for_justice_image, caption=rp.partners_for_justice_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_52):
        await bot.send_photo(message.from_user.id, photo=rp.misaeng_incomplete_life_image, caption=rp.misaeng_incomplete_life_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_53):
        await bot.send_photo(message.from_user.id, photo=rp.a_business_proposal_image, caption=rp.a_business_proposal_message)
        await bot.send_photo(message.from_user.id, photo=rp.my_father_is_strange_image, caption=rp.my_father_is_strange_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_54):
        await bot.send_photo(message.from_user.id, photo=rp.the_fiery_priest_image, caption=rp.the_fiery_priest_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_55):
        await bot.send_photo(message.from_user.id, photo=rp.my_name_image, caption=rp.my_name_message)
        await bot.send_photo(message.from_user.id, photo=rp.money_heist_korea_image, caption=rp.money_heist_korea_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_56):
        await bot.send_photo(message.from_user.id, photo=rp.chicago_typewriter_image, caption=rp.chicago_typewriter_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_57):
        await bot.send_photo(message.from_user.id, photo=rp.hot_stove_league_image, caption=rp.hot_stove_league_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_58):
        await bot.send_photo(message.from_user.id, photo=rp.strong_woman_do_bong_soon_image, caption=rp.strong_woman_do_bong_soon_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_59):
        await bot.send_photo(message.from_user.id, photo=rp.strangers_from_hell_image, caption=rp.strangers_from_hell_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_60):
        await bot.send_photo(message.from_user.id, photo=rp.love_to_hate_you_image, caption=rp.love_to_hate_you_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_61):
        await bot.send_photo(message.from_user.id, photo=rp.jewel_in_the_palace_image, caption=rp.jewel_in_the_palace_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_62):
        await bot.send_photo(message.from_user.id, photo=rp.tunnel_image, caption=rp.tunnel_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_63):
        await bot.send_photo(message.from_user.id, photo=rp.descendants_of_the_sun_image, caption=rp.descendants_of_the_sun_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_64):
        await bot.send_photo(message.from_user.id, photo=rp.hotel_del_luna_image, caption=rp.hotel_del_luna_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_65):
        await bot.send_photo(message.from_user.id, photo=rp.the_first_responders_image, caption=rp.the_first_responders_message)
        await bot.send_photo(message.from_user.id, photo=rp.little_women_image, caption=rp.little_women_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_66):
        await bot.send_photo(message.from_user.id, photo=rp.ghost_doctor_image, caption=rp.ghost_doctor_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_67):
        await bot.send_photo(message.from_user.id, photo=rp.reborn_rich_image, caption=rp.reborn_rich_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_68):
        await bot.send_photo(message.from_user.id, photo=rp.good_manager_image, caption=rp.good_manager_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_69):
        await bot.send_photo(message.from_user.id, photo=rp.the_bridal_mask_image, caption=rp.the_bridal_mask_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_70):
        await bot.send_photo(message.from_user.id, photo=rp.empress_ki_image, caption=rp.empress_ki_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_71):
        await bot.send_photo(message.from_user.id, photo=rp.go_back_couple_image, caption=rp.go_back_couple_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_72):
        await bot.send_photo(message.from_user.id, photo=rp.juvenile_justice_image, caption=rp.juvenile_justice_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_73):
        await bot.send_photo(message.from_user.id, photo=rp.designated_survivor_60_days_image, caption=rp.designated_survivor_60_days_message,
                             reply_markup=mp.finish_markup)

    elif sorted(genres_list) == sorted(rp.list_74):
        await bot.send_photo(message.from_user.id, photo=rp.cruel_city_image, caption=rp.cruel_city_message,
                             reply_markup=mp.finish_markup)

    else:
        await bot.send_message(message.from_user.id, text=rp.oops_message)


@dp.callback_query_handler(lambda c: c.data == "finish_button")
async def finish_callback(message: types.Message):
    await bot.send_message(message.from_user.id, text=rp.finish_message)


if __name__ == '__main__':
    executor.start_polling(dp)
