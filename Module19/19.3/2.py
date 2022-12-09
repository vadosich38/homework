players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

for i_player in players_dict.values():
    if i_player['team'] == "A" and i_player['status'] == 'Rest':
        print("Член команды А, который отдыхает:\n", i_player)
    elif i_player['team'] == "B" and i_player['status'] == 'Training':
        print("Член команды B, который тренируется:\n", i_player)
    elif i_player['team'] == "C" and i_player['status'] == 'Travel':
        print("Член команды C, который путешествует:\n", i_player)
