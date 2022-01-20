from main import *
from database import *

START_TIME = 8
END_TIME = 20

class UIFunctions():
    
    def toggleMenu(self, maxWidth, enable):
        if enable:
            
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 0

            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    
    def add_item_toBox(box,i,item):
        box.addItem("") #add lugar pro item 
        box.setItemText(i,item)

    def fill_clientBoxes(box):
        #clear the box previously filled
        box.clear()

        #get all user ordered by name
        users_name = BANCO_DADOS.select("*", "users", "name")

        #fill box with all users
        for i in range(0, len(users_name)):
            UIFunctions.add_item_toBox(box, i, users_name[i]["name"])

    def fill_schedule_box(ui_schedules_box,date):
        #clear the box previously filled
        ui_schedules_box.clear() 
        where = "s.scheduled_id = a.scheduled_id and a.date_id = '" + date + "'"

        #get the whole schedule from date
        schedules = BANCO_DADOS.select("s.scheduled","arrange a, schedule s", None, where)
        
        for i in range(0,len(schedules)):
            UIFunctions.add_item_toBox(ui_schedules_box, i, schedules[i]["scheduled"])

    def format_date_toDatabase(calendar):
        selected_date = str(calendar.selectedDate())
        print(selected_date)
        aux = selected_date.split("(")
        aux = aux[1].split(", ")
        ano = aux[0]
        mes = aux[1]
        dia = aux[2].split(")")
        dia = dia[0]
        
        format_data_db =  ano + "-" + mes + "-" + dia
        return format_data_db

    def add_schedules_toDatabase(date):
        #try to insert the date,
        #if 'error' get True means that already exist this date
        #if get False doesnt exist
        error = BANCO_DADOS.insert(date,"date")
        
        #Insert all store schedules
        if(error == False):
            for i in range(START_TIME,END_TIME):
                hr = str(i) + ":00"
                if(len(str(i)) == 1):
                    hr = "0" + hr
                
                BANCO_DADOS.insert(hr,"schedule")
                
                id_horario = len(BANCO_DADOS.select("scheduled_id","schedule"))
                BANCO_DADOS.insert_foreign_key(date,id_horario,"arrange")
 
class user:
    def add_new(self): 
        #create a list with each data from new user
        new_user_data = [self.ui.input_nome_newuser.text(), 
                         self.ui.input_tel_newuser.text(),
                         self.ui.input_lograd_newuser.text(),
                         self.ui.input_num_newuser.text(),
                         self.ui.input_compl_newuser.text(),
                         self.ui.input_cep_newuser.text()
                        ]
        
        #print(self.ui.input_nome_newuser.text())
        #insert it on database
        BANCO_DADOS.insert(new_user_data, "users")
        
        #clear all inputs for the next user
        self.ui.input_nome_newuser.clear()
        self.ui.input_tel_newuser.setText("(11) ")
        self.ui.input_lograd_newuser.clear()
        self.ui.input_num_newuser.clear()
        self.ui.input_compl_newuser.clear()
        self.ui.input_cep_newuser.clear()

    def edit(self):
        #get selected name
        name = self.ui.caixa_nomes_edit.currentText()

        #get id to update
        user_id = BANCO_DADOS.select("user_id", "users", None, "name = '" + name + "'")
        
        BANCO_DADOS.update({"name": self.ui.input_nome_edit.text(),
                            "phone": self.ui.input_tel_edit.text(),
                            "address": self.ui.input_lograd_edit.text(),
                            "address_number": self.ui.input_num_edit.text(),
                            "address_complement": self.ui.input_compl_edit.text(),
                            "cep": self.ui.input_cep_edit.text()},
                            "users", "user_id = " + str(user_id[0]["user_id"]))

    def fill_edit_inputs(self):
        #get selected user to edit
        user_name = self.ui.caixa_nomes_edit.currentText()

        if(user_name != ''): 
            dados = BANCO_DADOS.select("*", "users", None, "name = '" + user_name + "'")
            self.ui.input_nome_edit.setText(dados[0]["name"])
            self.ui.input_tel_edit.setText(dados[0]["phone"])
            self.ui.input_lograd_edit.setText(dados[0]["address"])
            self.ui.input_num_edit.setText(dados[0]["address_number"])
            self.ui.input_compl_edit.setText(dados[0]["address_complement"])
            self.ui.input_cep_edit.setText(dados[0]["cep"])

    def delete(box_names):
        #get selected name
        name = box_names.currentText()

        #get id to delete
        id = BANCO_DADOS.select("user_id", "users", None, "name = '" + name + "'")
        BANCO_DADOS.delete("users","user_id = " + str(id[0]["user_id"]))

class stock:

    def show_items(stock_items):
        stock_items.clear()
        #global listinha #??
        items_data = BANCO_DADOS.select("*","stock","name")
        list = []
        
        for i in range(0,len(items_data)):  
            #add each item name and quantity to a list
            list.append(items_data[i]["name"]+ " (" + str(items_data[i]["amount"]) + ")")
        
        stock_items.addItems(list)

    def add_new_item(self):
        new_data = [self.ui.input_nomeItem_additem.text(), self.ui.input_qntdinicial_additem.text()]
        BANCO_DADOS.insert(new_data, "stock")
        stock.show_items(self.ui.lista_estoque)

        #clear inputs for the next time
        self.ui.input_nomeItem_additem.clear()
        self.ui.input_qntdinicial_additem.clear()

    def modify_item_quantity(ui_items_box):
        ui_items_box.clear()
        #global caixinha #??

        #dictionaries with all items ordered by name
        items_data = BANCO_DADOS.select("*", "stock", "name")
        
        for v in range(0, len(items_data)):
            ui_items_box.addItem("") #add lugar pro item 
            ui_items_box.setItemText( #add o item
                v,
                items_data[v]["name"] + " (" + str(items_data[v]["amount"]) + ")")

        #fazer obotao desseelcionar qnd selecionar novo item
        #if ui_items_box.leaveEvent(ui_items_box.currentText()):
            #self.ui.rBtn_add_altqntd.setChecked(False)

        #self.ui.rBtn_ret_altqntd.clicked.connect(lambda: UIFunctions.check(self))
        #self.ui.rBtn_add_altqntd.clicked.connect(UIFunctions.check(self,1))
    
    def update_item_quantity(self):
        #get selected item    
        item = self.ui.caixa_itens_altqntd.currentText()

        item_name = item.split(" (")
        current_quantity = item_name[1].split(")")

        #quantity received by the user
        new_quantity = int(self.ui.input_altqntd.text())

        #if add button is selected
        if(self.ui.rBtn_add_altqntd.isChecked()): 
            total_quantity = int(current_quantity[0]) + new_quantity

        #if remove button is selected    
        if(self.ui.rBtn_ret_altqntd.isChecked()):
            total_quantity = int(current_quantity[0]) - new_quantity
            
            if total_quantity < 0:
                total_quantity = 0

        #get ids to update them
        ids = BANCO_DADOS.select("item_id", "stock", None, "name = '" + item_name[0]+ "'")
        BANCO_DADOS.update({"amount":str(total_quantity)}, "stock", "item_id = " + str(ids[0]["item_id"]))

        #show updated items
        stock.show_items(self.ui.lista_estoque)

        self.ui.input_altqntd.clear()

class toSchedule:

    def ddmmyyyy_date(date_toFormat):
        date = date_toFormat.split('-')
        year = date[0]

        month = date[1]
        day = date[2]

        if len(str(day)) == 1:
            day = "0" + day
        if len(str(month)) == 1:
            month = "0" + month
        date = day + "/" + month + "/" + str(year)

        return date

    def show_date(self):
        
        formated_date = UIFunctions.format_date_toDatabase(self.ui.calendario_agendar)
        
        UIFunctions.add_schedules_toDatabase(formated_date)
        UIFunctions.fill_schedule_box(self.ui.caixa_agendar_horarios, formated_date)

        date = toSchedule.ddmmyyyy_date(formated_date)

        #self.ui.label_agendar
        self.ui.label_dataselect.setText("Horários para o dia: " + date)
    
    #format string to arrange the appointment
    #Ex: 08:00 (Vick: M, P)
    def arrange_theAppointment(hour_selected, user_name, self):
        arrange = hour_selected + ":00 ("
        arrange += user_name + ": "
        
        #add the service to the arrange
        if(self.ui.checkBox_mao.isChecked()):
            arrange += "M, "
        if(self.ui.checkBox_pe.isChecked()):
            arrange += "P, "
        if(self.ui.checkBox_cabelo.isChecked()):
            arrange += "C, "
        if(self.ui.checkBox_unhagel.isChecked()):
            arrange += "UG, "

        #replace last , with )
        arrange = list(arrange)
        index_last_comma = len(arrange) - 2
        arrange[index_last_comma] = ')'
        arrange = "".join(arrange)
        
        return arrange

    def uncheck_services(self):
        if(self.ui.checkBox_mao.isChecked()):
            self.ui.checkBox_mao.setChecked(False)

        if(self.ui.checkBox_pe.isChecked()):
            self.ui.checkBox_pe.setChecked(False)

        if(self.ui.checkBox_cabelo.isChecked()):
            self.ui.checkBox_cabelo.setChecked(False)

        if(self.ui.checkBox_unhagel.isChecked()):
            self.ui.checkBox_unhagel.setChecked(False)

    def update_schedule(self):
        
        #get selected hour and format it
        aux = self.ui.caixa_agendar_horarios.currentText()
        hour_selected = aux.split(':')
        if(len(hour_selected[0]) == 1):
            hour_selected = "0" + hour_selected[0]
        else:
            hour_selected = hour_selected[0]

        #get selected date
        date = UIFunctions.format_date_toDatabase(self.ui.calendario_agendar)
        
        #get the first id from date
        first_id = BANCO_DADOS.select("scheduled_id","arrange",None, "date_id = '" + date + "' LIMIT 1")

        #equation to get hour id to update
        hour_id = first_id[0]["scheduled_id"] + int(hour_selected) - START_TIME
        
        #get user name selected
        user_name = self.ui.caixa_agendar_nomes.currentText()

        #get the arrangement with hour and service(s)
        arrange = toSchedule.arrange_theAppointment(hour_selected,user_name,self)

        BANCO_DADOS.update({"scheduled":arrange},"schedule", "scheduled_id = '" + str(hour_id) + "'")

        UIFunctions.fill_schedule_box(self.ui.caixa_agendar_horarios,date)
        toSchedule.uncheck_services(self)
