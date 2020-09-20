from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.test import Test


@dp.message_handler(Command("test"))
# or u can use this shit to test @dp.message_handler(text='/test') but variant higher is more short
async def enter_test(message: types.Message):
    await message.answer('U start test.\n'
                         'did u get some test? \n\n')
                #thats question


    await Test.Q1.set()#thats remembering of test in Q1(test.py)


@dp.message_handler(state=Test.Q1)# that start second question and startpoint its test.q1
async def answer_q1(message: types.Message, state: FSMContext): #FCMContent can make saving of answer in machine memory
    answer = message.text

    await state.update_data(answer1=answer)
    # async with state.proxy() as data: #thats another variant but u can use it when u need to change immediatly
    #     data["answer1"]  = answer


    await message.answer('Second quest \n'
                     'thats preambula \n')
    await Test.next()
    #await Test.Q2.set()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text

    await message.answer("Tnx for answer")
    await message.answer(f"1 answer: {answer1}")
    await message.answer(f"2 answer: {answer2}")

    await state.finish()
    #thats shit dropping data and block state

    #await state.reset_state()
    #thats another variant of stopping getting data

    #await state.reset_state(with_data=False)
    # #thats shit makes state false but without deleting data
