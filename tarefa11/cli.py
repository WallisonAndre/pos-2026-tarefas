import argparse
import users_wrapper as users

def main():
    p = argparse.ArgumentParser(description="Massa de manobra pro json placeholder")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list")

    r_p = sub.add_parser("read")
    r_p.add_argument("id", type=int)

    c_p = sub.add_parser("create")
    c_p.add_argument("--name", required=True)
    c_p.add_argument("--email", required=True)

    u_p = sub.add_parser("update")
    u_p.add_argument("id", type=int)
    u_p.add_argument("--name", default=None)
    u_p.add_argument("--email", default=None)

    d_p = sub.add_parser("delete")
    d_p.add_argument("id", type=int)

    args = p.parse_args()

    if args.cmd == "list":
        print(users.list())

    elif args.cmd == "read":
        print(users.read(args.id))

    elif args.cmd == "create":
        dados = {"name": args.name, "email": args.email}
        print("Criado:", users.create(dados))

    elif args.cmd == "update":
        dados = {}
        if args.name is not None: 
            dados["name"] = args.name
        if args.email is not None: 
            dados["email"] = args.email
        
        if len(dados) == 0:
            print("Manda alguma coisa pra atualizar!")
        else:
            print("Atualizado:", users.update(args.id, dados))

    elif args.cmd == "delete":
        if users.delete(args.id):
            print("Usuário deletado de boa")
        else:
            print("Deu erro ao deletar")

if __name__ == "__main__":
    main()