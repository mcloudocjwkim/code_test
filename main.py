
import sys
from pathlib import Path
from app.task_manager import TaskManager


if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "tasks.json"


def main():
    manager = TaskManager(DATA_FILE)

    while True:
        print("\n===== 업무 관리 프로그램 =====")
        print("1. 할 일 등록")
        print("2. 할 일 목록")
        print("3. 할 일 완료")
        print("4. 할 일 삭제")
        print("0. 종료")

        choice = input("선택: ").strip()

        if choice == "1":
            title = input("할 일: ").strip()
            if title:
                task_id = manager.add(title)
                print(f"등록 완료: {task_id}")

        elif choice == "2":
            tasks = manager.list_all()

            for task in tasks:
                status = "완료" if task["completed"] else "진행 중"
                print(
                    f'{task["id"]}. {task["title"]} [{status}]'
                )

            if not tasks:
                print("등록된 할 일이 없습니다.")

        elif choice == "3":
            task_id = int(input("완료할 번호: "))
            print("완료 처리했습니다." if manager.complete(task_id)
                  else "해당 작업을 찾지 못했습니다.")

        elif choice == "4":
            task_id = int(input("삭제할 번호: "))
            print("삭제했습니다." if manager.delete(task_id)
                  else "해당 작업을 찾지 못했습니다.")

        elif choice == "0":
            break

        else:
            print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
