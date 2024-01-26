import connexion
import os


if __name__ == '__main__':
    print(f'Starting server')


    try:
        app = connexion.App(__name__, specification_dir='./')
        file_path = os.path.dirname(__file__)
        app.add_api(file_path + '/open_api.yaml')
        app.run(port=8080)
    except Exception as e:
        print(f'Error: {e}')
