import sqlite3



class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status = True):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `student` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `student` WHERE `user_id` = ?', (user_id, )).fetchall()
            return bool(len(result))

    def subscriber_group(self, group):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `student` WHERE `group` = ?', (group, )).fetchall()
            return bool(len(result))

    def subscriber_exi(self, user_id):
    	from MNU_college_bot import bot
    	"""Проверяем, есть ли уже юзер в базе"""
    	with self.connection:
    		result = self.cursor.execute('SELECT * FROM `student` WHERE `user_id` = ?', (user_id, )).fetchall()
    		return bool(len(result))
    		aa = self.cursor.execute("SELECT * FROM student WHERE user_id = ?", (user_id,))
    		print(aa)
    		#bot.send_message(user_id, 'Вы из ', aa)
    	with self.connection:    
		    cur = self.cursor()    
		    self.cur.execute("SELECT * FROM 'student'")
		    rows = cur.fetchall()
		 
		    for row in rows:
		        print (row)
    def add_subscriber(self, user_id, course = True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `student` (`user_id`, `course`) VALUES(?,?)", (user_id,course))
    def add_group(self, user_id,  group, user_name,rank):
    	with self.connection:
    		return self.cursor.execute("INSERT INTO `student` (`user_id`, 'group','username','rank') VALUES(?,?,?,?)", (user_id, group, user_name, rank))

    def update_subscription(self, user_id, course):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `student` SET `status` = ? WHERE `user_id` = ?", (course, user_id))

    			#await bot.send_message(ass)
    def get_roz(self, group = "155"):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `розклад` WHERE `group` = ?", (group,)).fetchall()
    def get_ros(self, user_id):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `student` WHERE `user_id` = ?", (user_id,)).fetchall()
    def get_group(self, group):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `student` WHERE `group` = ?", (group,)).fetchall()

    def update_sqlite_table(self, course, user_id):
    	with self.connection:
		    try:#[5]
		        
		        print("Подключен к SQLite")

		        sql_update_query = """UPDATE student set course = ? where user_id = ?"""
		        data = (course, user_id)
		        self.cursor.execute(sql_update_query, data)
		        self.connection.commit()
		        print("Запись успешно обновлена")
		        

		    except sqlite3.Error as error:
		        print("Ошибка при работе с SQLite", error)
		    finally:
		        if self.connection:
		            self.connection.commit()
		            print("Соединение с SQLite закрыто")
    def what_group(self, user_id):
        with self.connection:
            try:
                sqlite_select_query = """SELECT * from student WHERE user_id = ?"""
                self.cursor.execute(sqlite_select_query, (user_id,))
                records = self.cursor.fetchall()
                #print(rec)
                for row in records:
                    print("ID:", row)
                    b = row[1]
                    a = row[2]
                    c = str(b)+str(a)

                    return c
                    #print("Имя:", row[1])
                    #print("Почта:", row[2])
                    #print("Добавлен:", row[3])
                    #print("Зарплата:", row[4], end="\n\n") get_group


            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)

    def new_course(self):
        with self.connection:
            try:
                sqlite_select_query = """SELECT * from student"""
                self.cursor.execute(sqlite_select_query)
                records = self.cursor.fetchall()
                #print(rec)
                for row in records:
                    print(row)
                    a = row[1]
                    if a[0] == "1":
                        a0 = a[0]
                        a2 = a[1:]
                        b = int(a0) +1
                        f = str(b) +a2


                        self.cursor.execute("UPDATE student set course = ?",(f,))
                        self.connection.commit()
                        return a
                    elif a[0] == "2":
                        a0 = a[0]
                        a2 = a[1:]
                        b = int(a0) +1
                        f = str(b) +a2
                        self.cursor.execute("UPDATE student set course = ?",(f,))
                        self.connection.commit()
                        return a
                    elif a[0] == "3":
                        a0 = a[0]
                        a2 = a[1:]
                        b = int(a0) +1
                        f = str(b) +a2
                        self.cursor.execute("UPDATE student set course = ?",(f,))
                        self.connection.commit()
                        return a
                    
                    else:
                        self.cursor.execute("UPDATE student set course = ?",("cancel",))
                        self.connection.commit()
                        
                        a = "Поздравляю с окончанием колледжа..."
                        return a
                    print("in "+ a+ "to"+f)

                slit = """SELECT * FROM starostat"""
                self.cursor.execute(sqlit)
                recordown = self.cursor.fetchall()
                for row in recordown:
                    group = row[1]
                    if group == '1':
                        a0 = a[0]
                        a2 = a[1:]
                        b = int(a0) +1
                        f = str(b) +a2
                        self.cursor.execute("UPDATE starostat set group = ?",(f,))
                        self.connection.commit()
                        return group
                    elif group == "2":
                        a0 = a[0]
                        a2 = a[1:]
                        b = int(a0) +1
                        f = str(b) +a2
                        self.cursor.execute("UPDATE starostat set group = ?",(f,))
                        self.connection.commit()
                    elif group == "3":
                        a0 = a[0]
                        a2 = a[1:]
                        b = int(a0) +1
                        f = str(b) +a2
                        self.cursor.execute("UPDATE starostat set group = ?",(f,))
                        self.connection.commit()
                    elif group == "4":
                        a0 = a[0]
                        a2 = a[1:]
                        b = int(a0) +1
                        f = str(b) +a2
                        self.cursor.execute("UPDATE starostat set group = ?",("cancel",))
                        self.connection.commit()
                    else:
                        pass
                        #print("Имя:", row[1])
                        #print("Почта:", row[2])
                        #print("Добавлен:", row[3])
                        #print("Зарплата:", row[4], end="\n\n") get_group



            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
    def starostat(self, user_id):
        with self.connection:
            sqlite = """SELECT * FROM rank"""
            self.cursor.execute(sqlite)
            record = self.cursor.fetchall()
            for row in record:
                rank = row[3]
                if rank == "creator":
                    user_id = row[0]
                    return user_id
    def starostat_admin(self, user_id):
        with self.connection:
            sqlite = """SELECT * FROM rank"""
            self.cursor.execute(sqlite)
            record = self.cursor.fetchall()
            for row in record:
                rank = row[3]
                if rank == "admin":
                    user_id = row[0]
                    return user_id
    def starostat(self, user_id):
        with self.connection:
            sqlite = """SELECT * FROM rank"""
            self.cursor.execute(sqlite)
            record = self.cursor.fetchall()
            for row in record:
                rank = row[3]
                if rank == "starosta":
                    user_id = row[0]
                    return user_id
    def starostat(self, user_id):
        with self.connection:
            sqlite = """SELECT * FROM rank"""
            self.cursor.execute(sqlite)
            record = self.cursor.fetchall()
            for row in record:
                rank = row[3]
                if rank == "head":
                    user_id = row[0]
                    return user_id
    def group(self,user_id):
        with self.connection:
            sqlite_select_query = """SELECT * from student WHERE user_id = ?"""
            #return bool(len(result))

            self.cursor.execute(sqlite_select_query, (user_id,))
            records = self.cursor.fetchall()
            #print(rec)
            for row in records:
                #print("ID:", row)
                a = row[1]
                return a
    def update_rank(self, user_id, rank):
        with self.connection:
            #sqlite_select_query = """SELECT * from student WHERE user_id = ?"""
            #self.cursor.execute(sqlite_select_query, (user_id,))
            #records = self.cursor.fetchall()
            self.cursor.execute("UPDATE student set rank = ? WHERE user_id = ?",(rank,user_id,))
            self.connection.commit()
    def what_rank(self, user_id):
        with self.connection:
            try:
                sqlite_select_query = """SELECT * from student WHERE user_id = ?"""
                self.cursor.execute(sqlite_select_query, (user_id,))
                records = self.cursor.fetchall()
                #print(rec)
                for row in records:
                    #print("ID:", row)
                    #b = row[0]
                    a = row[5]
                    c = str(a)#+str(a)
                    return c
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
    def all_rank(self, rank):
        sql_select_query = """SELECT * FROM student WHERE rank = ?"""
        self.cursor.execute(sql_select_query, (rank,))
        records = self.cursor.fetchall()
        return records
    def set_curator(self,user_id, group):
        with self.connection:
            return self.cursor.execute("INSERT INTO `curator` (`user_id`, `group`) VALUES(?,?)", (user_id,group))
    def set_permis(self, user_id, permision):
        with self.connection:
            if permision == "admin":
                sqlite_select_query = """SELECT * from student WHERE user_id = ?"""
                self.cursor.execute(sqlite_select_query, (user_id,))
                records = self.cursor.fetchall()
                if records == True:
                    self.cursor.execute("UPDATE student set rank = ? WHERE user_id = ?",(permision,user_id,))
                    self.connection.commit()
                else:
                    self.cursor.execute("INSERT INTO `starostat` (`user_id`, 'rank') VALUES(?,?)", (user_id,permision))
                    self.connection.commit()
            if permision == "starosta":
                sqlite_select_query = """SELECT * from starostat WHERE user_id = ?"""
                self.cursor.execute(sqlite_select_query, (user_id,))
                records = self.cursor.fetchall()
                if records == False:
                    self.cursor.execute("INSERT INTO `starostat` (`user_id`, 'group') VALUES(?,?)", (user_id,permision))
                    self.connection.commit()
                else:
                    self.cursor.execute("UPDATE student set rank = ? WHERE user_id = ?",(permision,user_id,))
            
    def what_id(self, user_id):
        with self.connection:
            sqlite_select_query = """SELECT * from student WHERE user_id = ?"""
            self.cursor.execute(sqlite_select_query, (user_id,))
            records = self.cursor.fetchall()
            return bool(len(records))
    def what_star(self, user_id):
        with self.connection:
            sqlite_select_query = """SELECT * from starostat WHERE user_id = ?"""
            self.cursor.execute(sqlite_select_query, (user_id,))
            records = self.cursor.fetchall()
            return bool(len(records))

    def close(self):
        self.connection.close()