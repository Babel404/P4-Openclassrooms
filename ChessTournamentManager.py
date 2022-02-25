from Controllers.Main_Controller import MainController
from Views.Menu import program_title


def main():
    program_title()
    controller = MainController()
    controller.load_database()


if __name__ == '__main__':
    main()
