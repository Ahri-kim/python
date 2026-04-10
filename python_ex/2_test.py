import oracledb
from person import Person

dsn = oracledb.makedsn("localhost", 1521, service_name="XE")
conn = oracledb.connect(user="c##mbc", password="qwer1234", dsn=dsn)

cursor = conn.cursor()
dirty = True
P = []

def show_menu():
    print("--임직원 관리 시스템--")
    print("- 1. 직원 추가 -")
    print("- 2. 직원 삭제  -")
    print("- 3. 직원 조회  -")
    print("- 4. 프로그램 종료 -")
    menu_num = input("메뉴를 선택해 주세요.")
    print(menu_num)
    return menu_num

def insert_emp():
    global dirty
    print("새로운 직원의 사번, 이름을 입력하세요....")
    empno, ename = input().split()
    print(empno, ename)

    if empno.isdigit():
        try:
            cursor.execute("INSERT INTO EMP (EMPNO, ENAME) VALUES (:1, :2)", [empno, ename.upper()])
            conn.commit()
            print("Data inserted successfully")
            dirty = True 

        except oracledb.DatabaseError as e:
            print(f"Error inserting data: {e}")
    else:
        print("AHRI-0001 : 사번 입력 오류 입니다. 숫자만 입력 가능합니다.")


def search_emp():
    global P, dirty
    if dirty or len(P) == 0:
        try:
            P.clear()
            cursor.execute('''SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO   
                FROM emp 
                ORDER BY EMPNO''')
            for row in cursor:
                p = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                P.append(p)
            dirty = False

        except oracledb.DatabaseError as e:
            print(f"Error fetching data: {e}")
    for p in P:
        p.print_person()

def delete_emp():
    global dirty
    print("삭제하려는 직원의 사번, 이름을 입력하세요.")
    empno, ename = input().split()
    try:
        cursor.execute("DELETE FROM emp WHERE empno = :empno and ename = :ename", [empno, ename.upper()])
        conn.commit()
        print("Data deleted successfully")
        dirty = True 

    except oracledb.DatabaseError as e:
        print(f"Error deleting data: {e}")

loop = True
while loop:
    select = int(show_menu())
    if select == 1:
        print("1. 직원 추가 메뉴")
        insert_emp()
    elif select == 2:
        print("2. 직원 삭제 메뉴")
        delete_emp()
    elif select == 3:
        print("3. 직원 조회 메뉴")
        search_emp()
    else:
        print("프로그램 종료***")
        loop = False

# 커서 및 커넥션 닫기
cursor.close()
conn.close()