from database import Database
from teacher_crud import TeacherCRUD

def main():
    db = Database("bolt://54.145.145.82", "neo4j", "mugs-aim-answer")
    teacher_crud = TeacherCRUD(db)

    # Criar Teacher Chris Lima
    teacher_crud.create("Chris Lima", 1956, "189.052.396-66")

    # Ler Teacher Chris Lima
    teacher = teacher_crud.read("Chris Lima")
    print("Teacher encontrado:", teacher)

    # Atualizar CPF de Chris Lima
    teacher_crud.update("Chris Lima", "162.052.777-77")
    print("CPF atualizado para Chris Lima.")

    # Deletar Chris Lima
    teacher_crud.delete("Chris Lima")
    print("Chris Lima foi deletado.")

    db.close()

if __name__ == "__main__":
    main()
