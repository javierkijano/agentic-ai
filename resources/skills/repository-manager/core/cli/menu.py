#!/usr/bin/env python3
import os
import sys
import pathlib

# Configurar paths para importar lógica
core_dir = pathlib.Path(__file__).parent.parent
sys.path.append(str(core_dir / "logic"))

# Imports de lógica (asumiendo que los archivos están en core/logic/)
from explorer import RepoExplorer
from doc_expert import DocExpert
# Nota: Importamos el resto según sea necesario

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    print("="*60)
    print("      AGENTIC RESOURCES - REPOSITORY COMMAND CENTER")
    print("="*60)

def main_menu():
    repo_root = core_dir.parent.parent.parent.parent
    explorer = RepoExplorer(repo_root)
    docs = DocExpert(repo_root)

    while True:
        clear_screen()
        print_header()
        print("\n[1] EXPLORAR: Listar habilidades y recursos")
        print("[2] DOCUMENTACIÓN: Consultar guías y reglas")
        print("[3] INTEGRIDAD: Validar estructura y limpieza")
        print("[4] GESTIÓN: Crear recurso o Generar Infra")
        print("[5] GIT: Preparar mensaje de commit")
        print("\n[0] SALIR")
        
        choice = input("\nSeleccione una opción: ")

        if choice == '1':
            clear_screen()
            print("--- INVENTARIO DE RECURSOS ---")
            for res in explorer.list_all_resources():
                print(f"[{res['kind'].upper()}] {res['id']}: {res['description'][:50]}...")
            input("\nPresione Enter para volver...")

        elif choice == '2':
            clear_screen()
            print("--- DOCUMENTACIÓN DISPONIBLE ---")
            available_docs = docs.list_docs()
            for i, d in enumerate(available_docs):
                print(f"[{i}] {d}")
            
            doc_choice = input("\nSeleccione un número para leer (o Enter para volver): ")
            if doc_choice.isdigit() and int(doc_choice) < len(available_docs):
                clear_screen()
                print(f"--- CONTENIDO DE {available_docs[int(doc_choice)]} ---\n")
                print(docs.read_doc(available_docs[int(doc_choice)]))
                input("\nPresione Enter para volver...")

        elif choice == '3':
            clear_screen()
            # Llamada al validador (importación local para evitar bucles)
            import validate_repo
            validate_repo.main() # Asumiendo que main existe
            input("\nPresione Enter para volver...")

        elif choice == '4':
            clear_screen()
            print("[1] Crear nuevo recurso")
            print("[2] Regenerar infraestructura (Docker/Pip)")
            m_choice = input("\nOpción: ")
            if m_choice == '1':
                rtype = input("Tipo (skills, agents, etc): ")
                rid = input("ID (kebab-case): ")
                import create_resource
                create_resource.create_resource(rtype, rid)
            elif m_choice == '2':
                rid = input("ID del recurso: ")
                # Buscar path del recurso y llamar a generate_infra
                import generate_infra
                # Aquí necesitaríamos lógica para encontrar el path, simplificado:
                # generate_infra.generate_infra(f'resources/skills/{rid}')
            input("\nPresione Enter para volver...")

        elif choice == '5':
            clear_screen()
            import describe_changes
            # Aquí necesitaríamos adaptar describe_changes para ser llamado como función
            os.system('python3 ' + str(core_dir / "logic/describe_changes.py"))
            input("\nPresione Enter para volver...")

        elif choice == '0':
            print("\n¡Hasta pronto!")
            break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario.")
