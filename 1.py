from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext


async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Углы", callback_data='angles'), InlineKeyboardButton("Треугольник", callback_data='triangle')],
        [InlineKeyboardButton("Многоугольники", callback_data='Polygons'), InlineKeyboardButton("Трапеция",callback_data='Trapezoid')],
        [InlineKeyboardButton("Параллелограмм", callback_data='Parallelogram'),InlineKeyboardButton("Ромб", callback_data='Rhomb')],
        [InlineKeyboardButton("Прямоугольник", callback_data='Rectangle'),InlineKeyboardButton("Квадрат", callback_data='Square')],
        [InlineKeyboardButton("Окружность", callback_data='The circle'),InlineKeyboardButton("Тригонометрия", callback_data='Trigonometry')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        await update.callback_query.edit_message_text('Выберите тему:', reply_markup=reply_markup)
    else:
        await update.message.reply_text('Выберите тему:', reply_markup=reply_markup)


async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    # Удаляем предыдущее сообщение с картинкой, если оно есть
    if 'last_photo_message_id' in context.user_data:
        try:
            await context.bot.delete_message(chat_id=query.message.chat_id, message_id=context.user_data['last_photo_message_id'])
        except Exception as e:
            print()



    if query.data == 'angles':
        await angles_menu(update, context)
    elif query.data == 'triangle':
        await triangle_menu(update, context)
    elif query.data == 'Polygons':
        await Polygons_menu(update, context)
    elif query.data == 'Trapezoid':
        await Trapezoid_menu(update, context)
    elif query.data == 'Parallelogram':
        await Parallelogram_menu(update, context)
    elif query.data == 'Rhomb':
        await Rhomb_menu(update, context)
    elif query.data == 'Rectangle':
        await Rectangle_menu(update, context)
    elif query.data == 'Square':
        await Square_menu(update, context)
    elif query.data == 'The circle':
        await The_circle_menu(update, context)
    elif query.data == 'Trigonometry':
        await The_Trigonometry_menu(update, context)



    #Углы
    elif query.data == 'types_of_angles':
        with open('1ugol-1.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'parallel_angles':
        with open('1ugol-2.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id

    #Треугольник
    elif query.data == 'types_of_triangles':
        with open('2treug-1.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'sum_of_angles':
        with open('2treug-2.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'bisector':
        with open('2treug-3.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'median':
        with open('2treug-4.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'height':
        with open('2treug-5.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'perpendicular_bisector':
        with open('2treug-6.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'midline':
        with open('2treug-7.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'triangle_inequality':
        with open('2treug-8.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'triangle_area':
        with open('2treug-9.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'sine+cosine_theorem':
        with open('2treug-10.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'equality_signs':
        with open('2treug-11.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'right_triangle_equality_signs':
        with open('2treug-12.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'similarity_signs':
        with open('2treug-13.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'similar_triangle_properties':
        with open('2treug-14.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'isosceles_triangle':
        with open('2treug-15.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'equilateral_triangle':
        with open('2treug-16.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'right_triangle':
        with open('2treug-17.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'relations in a right-angled triangle':
        with open('2treug-18.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id


    #Многоугольники
    elif query.data == 'Convex polygon':
        with open('3mnogoug-1.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'sum_of_angles2':
        with open('3mnogoug-2.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'A quadrilateral inscribed in a circle':
        with open('3mnogoug-3.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'A circle inscribed in a quadrilateral':
        with open('3mnogoug-4.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'Regular polygons':
        with open('3mnogoug-5.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id


    # Параллелограм
    elif query.data == 'Properties and attributes':
        with open('5paral-1.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'Corners_and_area2':
        with open('5paral-2.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id

    # Окружности
    elif query.data == 'Circumference and arc length':
        with open('9okr-1.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'The chord':
        with open('9okr-2.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'Inscribed and central corners':
        with open('9okr-3.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'The tangent':
        with open('9okr-4.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'Secant1':
        with open('9okr-5.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'Sector area and arc length':
        with open('9okr-6.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'The inscribed circle':
        with open('9okr-7.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'The circumscribed circle':
        with open('9okr-8.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id

    # Тригонометрия
    elif query.data == 'Sine,cosine,tangent,cotangent':
        with open('10trigon-1.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'Basic trigonometric identities':
        with open('10trigon-2.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'Conversion formulas':
        with open('10trigon-3.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id
    elif query.data == 'The values of the trigonometric functions of some angles':
        with open('10trigon-4.jpg', 'rb') as photo:
            message = await query.message.reply_photo(photo)
            context.user_data['last_photo_message_id'] = message.message_id



    #Назад
    elif query.data == 'back':
        await start(update, context)

#Углы
async def angles_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Виды углов", callback_data='types_of_angles')],
        [InlineKeyboardButton("Углы при параллельных прямых и секущей", callback_data='parallel_angles')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('Углы. Выберите подтему:', reply_markup=reply_markup)

# Треугольники
async def triangle_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Виды треугольников", callback_data='types_of_triangles'), InlineKeyboardButton("Сумма углов и внешний угол", callback_data='sum_of_angles')],
        [InlineKeyboardButton("Биссектриса", callback_data='bisector'), InlineKeyboardButton("Медиана", callback_data='median')],
        [InlineKeyboardButton("Высота", callback_data='height'), InlineKeyboardButton("Серединный перпендикуляр", callback_data='perpendicular_bisector')],
        [InlineKeyboardButton("Средняя линия", callback_data='midline'),InlineKeyboardButton("Площадь", callback_data='triangle_area')],
        [InlineKeyboardButton("Неравенство треугольника", callback_data='triangle_inequality')],
        [InlineKeyboardButton("Теоремы синусов и косинусов", callback_data='sine+cosine_theorem')],
        [InlineKeyboardButton("Признаки равенства", callback_data='equality_signs'),InlineKeyboardButton("Признаки подобия", callback_data='similarity_signs')],
        [InlineKeyboardButton("Признаки равенства прямоугольных треугольников", callback_data='right_triangle_equality_signs')],
        [InlineKeyboardButton("Свойства подобных треугольников", callback_data='similar_triangle_properties')],
        [InlineKeyboardButton("Равнобедренный", callback_data='isosceles_triangle'),InlineKeyboardButton("Равносторонний", callback_data='equilateral_triangle')],
        [InlineKeyboardButton("Прямоугольный", callback_data='right_triangle'),InlineKeyboardButton("Соотношения прям.тр.", callback_data='relations in a right-angled triangle')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('Треугольники. Выберите подтему:                               ', reply_markup=reply_markup)

#Многоугольники

async def Polygons_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Выпуклый многоугольник", callback_data='Convex polygon')],
        [InlineKeyboardButton("Площадь четырехугольника", callback_data='sum_of_angles2')],
        [InlineKeyboardButton("Четырехугольник, вписанный в окружность", callback_data='A quadrilateral inscribed in a circle')],
        [InlineKeyboardButton("Окружность, вписанная в четырехугольник", callback_data='A circle inscribed in a quadrilateral')],
        [InlineKeyboardButton("Правильные многоугольники", callback_data='Regular polygons')],
        [InlineKeyboardButton("Назад", callback_data='back')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('Многоугольники. Выберите подтему:', reply_markup=reply_markup)

#Трапеция
async def Trapezoid_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    with open('4trapec.jpg', 'rb') as photo:
        message = await query.message.reply_photo(photo)
        context.user_data['last_photo_message_id'] = message.message_id
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('В главное меню ↓', reply_markup=reply_markup)


#Параллелограм
async def Parallelogram_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Свойства и признаки параллелограмма", callback_data='Properties and attributes')],
        [InlineKeyboardButton("Углы и площадь параллелограмма", callback_data='Corners_and_area2')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('Параллелограмм. Выберите подтему:', reply_markup=reply_markup)


#Ромб
async def Rhomb_menu(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]

    with open('7romb.jpg', 'rb') as photo:
        message = await query.message.reply_photo(photo)
        context.user_data['last_photo_message_id'] = message.message_id

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('В главное меню ↓', reply_markup=reply_markup)

#Прямоугольники
async def Rectangle_menu(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]

    with open('6praym.jpg', 'rb') as photo:
        message = await query.message.reply_photo(photo)
        context.user_data['last_photo_message_id'] = message.message_id

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('В главное меню ↓', reply_markup=reply_markup)

#Квадраты
async def Square_menu(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]

    with open('8kvadr.jpg', 'rb') as photo:
        message = await query.message.reply_photo(photo)
        context.user_data['last_photo_message_id'] = message.message_id

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('В главное меню ↓', reply_markup=reply_markup)

#Окружности
async def The_circle_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Длина окружности и площадь круга", callback_data='Circumference and arc length')],
        [InlineKeyboardButton("Хорда", callback_data='The chord')],
        [InlineKeyboardButton("Вписанный и центральный уголы", callback_data='Inscribed and central corners')],
        [InlineKeyboardButton("Касательная", callback_data='The tangent')],
        [InlineKeyboardButton("Секущая", callback_data='Secant1')],
        [InlineKeyboardButton("Площадь сектора и длинна дуги", callback_data='Sector area and arc length')],
        [InlineKeyboardButton("Вписанная окружность", callback_data='The inscribed circle')],
        [InlineKeyboardButton("Описанная окружность", callback_data='The circumscribed circle')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('Окружность. Выберите подтему:', reply_markup=reply_markup)

#Тригонометрия
async def The_Trigonometry_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Синус, косинус, тангенс, котангенс", callback_data='Sine,cosine,tangent,cotangent')],
        [InlineKeyboardButton("Тригонометрические тождества", callback_data='Basic trigonometric identities')],
        [InlineKeyboardButton("Формулы приведения", callback_data='Conversion formulas')],
        [InlineKeyboardButton("Значения тригонометрических функций углов", callback_data='The values of the trigonometric functions of some angles')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text('Тригонометрия. Выберите подтему:', reply_markup=reply_markup)



def main() -> None:
    application = Application.builder().token("7064007977:AAERAkiWxjjjglwhxDuqmf8TCM013T-4UqA").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()