from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout,QPushButton, QLabel, QTextEdit, QApplication,QListWidget,QLineEdit,QInputDialog
from PyQt5.QtCore import Qt
import json 


"""notes={"Ласкаво просимо!" : {
    "текст" : "Це найкращий додаток для заміток у світі!",
    "теги":["добро","інструкція"]
    }
}

with open("notes_data.json","w") as file:
    json.dump(notes,file)"""

app = QApplication([])
window = QWidget()

main_field=QTextEdit()

text_for_notes=QLabel("Список заміток")
notes_list=QListWidget()


create_note=QPushButton("Створити замітку")
del_note=QPushButton("Видалити замітку")
save_note=QPushButton("Зберегти замітку")
text_for_tags=QLabel("Список тегів")
tags_list=QListWidget()

field_text=QLineEdit()
field_text.setPlaceholderText("Введіть тег...")
create_tags=QPushButton("Додати до замітки")
del_tags=QPushButton("Відкріпити від замітки")
save_tags=QPushButton("Шукати замітку по тегу")





main_line=QVBoxLayout()
main_hor_line=QHBoxLayout()
hor1=QHBoxLayout()
hor1.addWidget(create_note)
hor1.addWidget(del_note)
hor2=QHBoxLayout()
hor2.addWidget(create_tags)
hor2.addWidget(del_tags)


main_line.addWidget(text_for_notes)
main_line.addWidget(notes_list)
main_line.addLayout(hor1)
main_line.addWidget(save_note)


main_hor_line.addWidget(main_field)



main_line.addWidget(text_for_tags)
main_line.addWidget(tags_list)
main_line.addWidget(field_text)
main_line.addLayout(hor2)
main_line.addWidget(save_tags)
main_hor_line.addLayout(main_line)
window.setLayout(main_hor_line)

def show_note():
    key=notes_list.selectedItems()[0].text()
    print(key)
    main_field.setText(notes[key]["текст"])
    tags_list.clear()
    tags_list.addItems(notes[key]["теги"])





def add_note():
    note_name, ok =QInputDialog.getText(window,"Додати замітку","Нова замітка:")
    if ok and note_name !="":
        notes[note_name]={"текст":"","теги":[]}
        notes_list.addItem(note_name)
        #tags_list.addItems(notes[note_name]["теги"])
        with open("notes_data.json","w") as file:
            json.dump(notes,file)



def delete_note():
    if notes_list.selectedItems():
        key=notes_list.selectedItems()[0].text()
        del notes[key]
        notes_list.clear()
        notes_list.addItems(notes)
        
    else:
            print("Замітка для видалення не вибрана!")

def save_notes():
    key=notes_list.selectedItems()[0].text()
    text=main_field.toPlainText()
    notes[key]['текст']=text
    with open("notes_data.json","w") as file:
            json.dump(notes,file)

def add_tag():
    if notes_list.selectedItems():
        key=notes_list.selectedItems()[0].text()
        tag=field_text.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            field_text.clear()
            tags_list.addItem(tag)
            with open("notes_data.json","w") as file:
                json.dump(notes,file,sort_keys=True)
        else:
            print("Замітка для додавання тега не вибрана!")

def del_tag():
    if tags_list.selectedItems():
        tag=tags_list.selectedItems()[0].text()
        key=notes_list.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
      
        tags_list.clear()
        tags_list.addItems(notes[key]['теги'])
        with open("notes_data.json","w") as file:
                json.dump(notes,file,sort_keys=True)


def search_tag():
    tag = field_text.text()
    print(tag)
    if save_tags.text() == "Шукати замітку по тегу" :
        
        notes_filtered =  []
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered.append(note)
        save_tags.setText("Скинути пошук")
        notes_list.clear()
        tags_list.clear()
        notes_list.addItems(notes_filtered)
    elif save_tags.text() == "Скинути пошук":
        tags_list.clear()
        notes_list.clear()
        tags_list.clear()
        notes_list.addItems(notes)
        save_tags.setText("Шукати замітку по тегу")
    else:
        pass
     









notes_list.itemClicked.connect(show_note)
create_tags.clicked.connect(add_tag)
del_note.clicked.connect(delete_note)
save_note.clicked.connect(save_notes)
del_tags.clicked.connect(del_tag)
save_tags.clicked.connect(search_tag)










with open("notes_data.json","r") as file:
    notes = json.load(file)
notes_list.addItems(notes)

create_note.clicked.connect(add_note)
window.resize(900, 600)
window.show()

app.exec_()