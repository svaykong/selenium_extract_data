if __name__ == '__main__':
    print('__main__ call')

    try:
        from dotenv import load_dotenv
        load_dotenv(override=True)

        from github_user import GithubUser

        user = GithubUser()
        user.login()

    except Exception as e:
        print(f'__main__ exception::{e}')
    finally:
        print(f'__main__ finally')
