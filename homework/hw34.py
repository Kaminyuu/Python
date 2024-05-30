from pc import Pc


def main():
    for i in range(1, 3):
        pars = Pc(f"https://www.ixbt.com/live/blog/games/page{i}/", "pc.txt")
        pars.run()


if __name__ == '__main__':
    main()
