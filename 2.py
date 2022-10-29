# Создайте программу для игры с конфетами человек против человека.

#Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def Player_vs_player(player1_candy, player2_candy):
	print('Игрок против игрока')
	candy = 2021
	while candy > 0:
		take1_candy = int(input('Ход Игрока 1: '))
		while take1_candy < 0 or take1_candy > 28:
			print('Брать можно только от 0 до 28 конфет!')
			take1_candy = int(input('Ход Игрока 1: '))
		while take1_candy > candy:
			print('В стопке недостаточно конфет!')
			take1_candy = int(input('Ход Игрока 1: '))
		else:
			if 0 <= take1_candy <= 28:
				player1_candy = player1_candy + take1_candy
				candy = candy - take1_candy
				print(f'У Игрока 1 {player1_candy} конфет')
				print(f'Конфет осталось: {candy}')
				if candy == 0:
					player1_candy = player1_candy + player2_candy
					print(f"Игрок 1 ПОБЕДИЛ!\nС количеством конфет: {player1_candy}")
					print("Игра окончена!")
					return
		take2_candy = int(input('Ход Игрока 2: '))
		while take2_candy <= 0 or take2_candy > 28:
			print('Брать можно только от 0 до 28 конфет!')
			take2_candy = int(input('Ход Игрока 2: '))
		while take2_candy > candy:
			print('В стопке недостаточно конфет!')
			take2_candy = int(input('Ход Игрока 2: '))
		else:
			if 0 <= take2_candy <= 28:
				player2_candy = take2_candy + player2_candy
				candy = candy - take2_candy
				print(f'У Игрока 2 {player2_candy} конфет')
				print(f'Конфет в стопке осталось: {candy}')
				if candy == 0:
					player2_candy = player2_candy + player1_candy
					print(f"Игрока 2 ПОБЕДИЛ!\nС количеством конфет: {player2_candy}")
					print("Игра окончена!")
					return

def Player_vs_computer(comp_candy, player_candy):
	print('Игрок против компьютера')
	candy = 2021
	while candy > 0:
		take1_candy = random.randint(0, 28)
		if take1_candy > candy:
			take1_candy = candy
		print(f' Компьютер берет {take1_candy} конфет')
		comp_candy = comp_candy + take1_candy
		candy = candy - take1_candy
		print(f'У Компьютера: {comp_candy} конфет')
		print(f'Конфет в стопке осталось: {candy}')
		if candy == 0:
			player1_candy = comp_candy + player_candy
			print(f"Компьютер ПОБЕДИЛ!\nС количеством конфет: {player1_candy}")
			print("Игра окончена!")
			return
		take2_candy = int(input('Ход Игрока: '))
		while take2_candy <= 0 or take2_candy > 28:
			print('Брать можно только от 0 до 28 конфет!')
			take2_candy = int(input('Ход Игрока: '))
		while take2_candy > candy:
			print('В стопке недостаточно конфет!')
			take2_candy = int(input('Ход Игрока: '))
		else:
			if 0 <= take2_candy <= 28:
				player_candy = take2_candy + player_candy
				candy = candy - take2_candy
				print(f'У Игрока {player_candy} конфет')
				print(f'Конфет в стопке осталось: {candy}')
				if candy == 0:
					player_candy = player_candy + comp_candy
					print(f"Игрок ПОБЕДИЛ!\nС количеством конфет: {player_candy}")
					print("Игра окончена!")
					return

def Chose_game_model(model):
	if model == 1:
		player1_candy = 0
		player2_candy = 0
		Player_vs_player(player1_candy, player2_candy)
	elif model == 2:
		comp_candy = 0
		player_candy = 0
		Player_vs_computer(comp_candy, player_candy)
	else:
		print("Нет такого режима!")


chose_model = int(input('Выбери режим игры:\n1 - Против другого игрока\n2 - Против компьютера\nВыбор: '))
Chose_game_model(chose_model)