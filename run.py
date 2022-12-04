from app.loader import ILoader, Loader


def main():
    loader: ILoader = Loader()
    loader.loader_painel_saneamento()


if __name__ == "__main__":
    main()
