import random

def beau_fav_anime(anime_list):
    print("Beau's Favourite anime is", random.choice(anime_list))
    beau_fav_anime != harry_fav_anime

def harry_fav_anime(anime_list):
    print("Harry's Favourite anime is", random.choice(anime_list))
    beau_fav_anime(anime_list)
    beau_fav_anime != harry_fav_anime

def main():
    anime_list = ["One Piece", "Naruto", "Black Clover", "Dragon Ball", "Bleach"]
    beau_fav_anime = random.choice(anime_list)
    harry_fav_anime = random.choice(anime_list)
    while True:
        if beau_fav_anime == harry_fav_anime:
            beau_fav_anime = random.choice(anime_list)
        else:
            break
        harry_fav_anime (anime_list)


main()
    # Beau's fav anime is One piece
    # Harry's fav anime is Naruto
