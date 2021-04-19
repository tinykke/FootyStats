from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
import datetime
from decimal import Decimal
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton, MDIconButton
from kivy.core.window import Window
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker

Window.size = (344,650)
''' Remove for final app '''

kv = """
BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        id: toolbar
        elevation: 10
        title: "AFL Stat Star"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["account-multiple-plus", lambda x: app.showAddPlayer_Dialog()]]


    NavigationLayout:
        ScreenManager:
            id: screen_manager
            HomeScreen:
                id: home
                name: 'home'
                manager: 'screen_manager'
                
            NScreen:
                
                id: stats
                name: 'stats'
                manager: 'screen_manager'

        MDNavigationDrawer:
            id: nav_drawer
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        icon: 'soccer'
                        text: "Home"
                        on_press:
                            nav_drawer.set_state("close")
                            screen_manager.current = "home"
                        IconLeftWidget:
                            icon: 'home'
                    OneLineIconListItem:
                        text: "Stats"
                        on_press:
                            nav_drawer.set_state("close")
                            screen_manager.current = "stats"
                        IconLeftWidget:
                            icon: 'football-australian'
<HomeScreen>:
    MDLabel:
        text: 'Home screen'
        halign: 'center'


<InfoCard>:  # put the MD Card in a seperate class
    display: display
    displayHandballs: displayHandballs
    displayMarks: displayMarks
    displayTackles: displayTackles
    displayClear: displayClear
    displayCont: displayCont
    displayDisp: displayDisp
    displayFant: displayFant
    displayScore: displayScore
    displayJumper: displayJumper
    orientation: "vertical"
    padding: "8dp"
    size_hint: None, None
    size: "320dp", "520dp"
    pos_hint: {"center_x": .5, "center_y": .5}
    on_release: app.show_example_custom_bottom_sheet()


    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        adaptive_width: True
          

        Image:
            source: 'body-shot.png'
            size_hint: None, None
            height: 70
            anchor_x: 'left' 
                        
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: None
            MDLabel:
                text: root.Jumper_content
                theme_text_color: "Primary"
                font_style: "H4"   
                size_hint_y: 20
                size_hint_x: 60

            MDLabel:
                id: displayJumper
                text: root.title
                theme_text_color: "Primary"
                size_hint_y: 20
                size_hint_x: 150
                height: self.texture_size[1]
                font_style: "H5"    
                anchor_x: 'left'
    

            MDLabel:
                text: root.GameDate_content
                theme_text_color: "Secondary"
                size_hint_y: 20
                height: self.texture_size[1]
                font_style: "Body2"

    MDSeparator:
        height: "1dp"

    FloatLayout:
        MDLabel:
            text: "Disposals"
            halign: "center"
            size_hint: 0.5, 0.6
            padding_y: 5
            pos_hint: {"center_x":0.15, "center_y": 0.2}


        MDLabel:
            canvas:
                Color:
                    rgba: (0,0,0,0.2)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [25]
            id: displayDisp
            text: root.Disp_content
            halign: "center"
            size_hint: 0.3, 0.4
            
            pos_hint: {"center_x":0.15, "center_y": 0.5}

    
        MDLabel:
            text: "Score"
            halign: "center"
            size_hint: 0.5, 0.6
            padding_y: 5
            pos_hint: {"center_x":0.50, "center_y": 0.2}


        MDLabel:
            canvas:
                Color:
                    rgba: (0,0,0,0.2)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [25]
            id: displayScore
            text: root.Score_content
            halign: "center"
            size_hint: 0.3, 0.4
            
            pos_hint: {"center_x":0.50, "center_y": 0.5}

        MDLabel:
            text: "Fantasy"
            halign: "center"
            size_hint: 0.5, 0.6
            padding_y: 5
            pos_hint: {"center_x":0.85, "center_y": 0.2}


        MDLabel:
            canvas:
                Color:
                    rgba: (0,0,0,0.2)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [25]
            id: displayFant
            text: root.Fant_content
            halign: "center"
            size_hint: 0.3, 0.4
            
            pos_hint: {"center_x":0.85, "center_y": 0.5}    


    BoxLayout:
        orientation: 'horizontal'
        size_hint_x: None
        spacing: "20dp"
        padding: "10dp"
        adaptive_width: True
        halign: "center"    

        MDCard:
            size_hint: None, None
            size: "85dp", "75dp"
            

            BoxLayout:
                orientation: 'vertical'
                
                spacing: "1dp" 
                MDLabel:
                    id: display
                    text: root.kicks_content
                    theme_text_color: "Primary"
                    halign: "center"
                    valign: "center"
                    font_style: "H4"
                    height: 20
                MDLabel:
                    height: 20
                    text: "Kicks"
                    theme_text_color: "Secondary"
                    halign: "center"

        MDCard:
            size_hint: None, None
            size: "85dp", "75dp"
            

            BoxLayout:
                orientation: 'vertical'
                
                spacing: "1dp" 
                MDLabel:
                    id: displayMarks
                    text: root.Marks_content
                    theme_text_color: "Primary"
                    halign: "center"
                    valign: "center"
                    font_style: "H4"
                    height: 20
                MDLabel:
                    height: 20
                    text: "Marks"
                    theme_text_color: "Secondary"
                    halign: "center"
                
        MDCard:
            size_hint: None, None
            size: "85dp", "75dp"
            

            BoxLayout:
                orientation: 'vertical'
                
                spacing: "1dp" 
                MDLabel:
                    id: displayHandballs
                    text: root.Handballs_content
                    theme_text_color: "Primary"
                    halign: "center"
                    valign: "center"
                    font_style: "H4"
                    height: 20
                MDLabel:
                    height: 20
                    text: "Handballs"
                    theme_text_color: "Secondary"
                    halign: "center"


    BoxLayout:
        orientation: 'horizontal'
        size_hint_x: None
        spacing: "20dp"
        padding: "10dp"
        adaptive_width: True
        halign: "center"    

        MDCard:
            size_hint: None, None
            size: "85dp", "75dp"
            

            BoxLayout:
                orientation: 'vertical'
                
                spacing: "1dp" 
                MDLabel:
                    id: displayTackles
                    text: root.Tackles_content
                    theme_text_color: "Primary"
                    halign: "center"
                    valign: "center"
                    font_style: "H4"
                    height: 20
                MDLabel:
                    height: 20
                    text: "Tackles"
                    theme_text_color: "Secondary"
                    halign: "center"

        MDCard:
            size_hint: None, None
            size: "85dp", "75dp"
            

            BoxLayout:
                orientation: 'vertical'
                
                spacing: "1dp" 
                MDLabel:
                    id: displayClear
                    text: root.Clear_content
                    theme_text_color: "Primary"
                    halign: "center"
                    valign: "center"
                    font_style: "H4"
                    height: 20
                MDLabel:
                    height: 20
                    text: "Clearance"
                    theme_text_color: "Secondary"
                    halign: "center"
                
        MDCard:
            size_hint: None, None
            size: "85dp", "75dp"
            

            BoxLayout:
                orientation: 'vertical'
                
                spacing: "1dp" 
                MDLabel:
                    id: displayCont
                    text: root.Cont_content
                    theme_text_color: "Primary"
                    halign: "center"
                    valign: "center"
                    font_style: "H4"
                    height: 20
                MDLabel:
                    height: 20
                    text: "Contested"
                    theme_text_color: "Secondary"
                    halign: "center"                    
                    
                   


        




      
    MDSeparator:
        height: "1dp"
    
        
    GridLayout:
        orientation: "lr-tb"
        rows: 4
        cols: 3
        adaptive_width: True
        spacing: 4
        padding: 3
        
        MDRectangleFlatButton:
            id: kick_button
            text: "KICK"
            text_color: 0, 0, 1, 1
            line_color: 0, 0, 1, 1
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: root.add_one()
        MDRectangleFlatButton:
            id: kick_button
            text: "Mark"
            size_hint_y: None
            theme_text_color: "Custom"
            text_color: 0, 0, 1, 1
            line_color: 0, 0, 1, 1
            on_release: root.add_oneMark()
        MDRectangleFlatButton:
            id: kick_button
            text: "Handball"
            theme_text_color: "Custom"
            text_color: 0, 0, 1, 1
            line_color: 0, 0, 1, 1
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: root.add_oneHandball()
        MDRectangleFlatButton:
            id: kick_button
            text: "Tackle"
            theme_text_color: "Custom"
            text_color: 0, 0, 1, 1
            line_color: 0, 0, 1, 1
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: root.add_oneTackle()
        MDRectangleFlatButton:
            id: kick_button
            text: "Clearances"
            theme_text_color: "Custom"
            text_color: 0, 0, 1, 1
            line_color: 0, 0, 1, 1
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: root.add_oneClear()
        MDRectangleFlatButton:
            id: kick_button
            text: "Contested"
            theme_text_color: "Custom"
            text_color: 0, 0, 1, 1
            line_color: 0, 0, 1, 1
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: root.add_oneCont()             
        MDFlatButton:
            text: "Goal"
            theme_text_color: "Custom"
            text_color: 0, 0, 1, 1  
            on_release: root.add_oneGoal() 
        MDFlatButton:
            text: "Point"
            theme_text_color: "Custom"
            text_color: 0, 0, 1, 1   
            on_release: root.add_onePoint()
        MDIconButton:
            icon: "account-remove"
            user_font_size: "32sp"
            on_release: root.delete_player()
        MDLabel:
            id: userID_content_label
            text: root.UserID_content
            size_hint: None, None
            size: "10dp", "10dp"
            height: 10
    
       
<ItemForCustomBottomSheet@OneLineIconListItem>
    on_press: app.custom_sheet.dismiss()
    icon: ""

    IconLeftWidget:
        icon: root.icon

<ContentCustomSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "450dp"

    MDToolbar:
        title: "Extra"

    ScrollView:

        MDGridLayout:
            cols: 1
            adaptive_height: True

            ItemForCustomBottomSheet:
                icon: "account-remove"
                text: "Delete"
                

                

            ItemForCustomBottomSheet:
                icon: "exit-to-app"
                text: "Exit"        
       

<NScreen>:
    on_pre_enter: self.set_title()
    ScrollView:
        do_scroll_x: True
        do_scroll_y: False
        scroll_type: ['bars', 'content']
        bar_width: '10dp'
        BoxLayout:
            padding: '20dp'
            spacing: '20dp'
            id: card_box
            width: self.minimum_width
            size_hint_x: None

<AddPlayerContent>
    playerNametxt: playerNametxt
    id: addplayercontent
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "300dp"

    MDTextField:
        id: playerNametxt
        hint_text: "Player Name"
        mode: "rectangle"
        helper_text_mode: "on_focus"

    MDTextField:
        id: Againsttxt
        hint_text: "Against"
        mode: "rectangle"

    MDRectangleFlatIconButton:
        icon: "calendar"
        text: "Game Date"
        on_release: root.show_date_picker()
            

    MDLabel:
        id: date_picker_label
        text: str(root.gamedate)


    BoxLayout:
        orientation: "horizontal"
    
        MDLabel:
            text: "Select Jumper Number"
        MDLabel:
            id: SliderJumpertxt
            text: str(int(SliderJumper.value))
        

    MDSlider:
        id: SliderJumper
        min: 1
        max: 100
        value: 40
        

        

        


    
"""

class AddButton(MDRectangleFlatButton):
    pass

class HomeScreen(Screen):
    pass

class AddPlayerContent(BoxLayout):
    gamedate = StringProperty()
    

    def get_date(self, the_date):
        gamedate = str(the_date.strftime("%d/%m/%Y"))
        print(gamedate)
        self.ids.date_picker_label.text=gamedate

       

    
    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        #date_dialog.bind(on_save=root.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


    


class InfoCard(MDCard):
    display = ObjectProperty()
    userID_content_label = ObjectProperty()
    displayHandballs = ObjectProperty()
    displayMarks = ObjectProperty()
    displayTackles = ObjectProperty()
    displayClear = ObjectProperty()
    displayCont = ObjectProperty()
    displayDisp = ObjectProperty()
    displayFant = ObjectProperty()
    displayScore = ObjectProperty()
    displayJumper = ObjectProperty()
    title = StringProperty()
    GameDate_content = StringProperty()
    kicks_content = StringProperty()
    UserID_content = StringProperty()
    Handballs_content = StringProperty()
    Marks_content = StringProperty()
    Tackles_content = StringProperty()
    Clear_content = StringProperty()
    Cont_content = StringProperty()
    Disp_content = StringProperty()
    Fant_content = StringProperty()
    Score_content = StringProperty()
    Jumper_content = StringProperty()
    

    def add_one(self):
        #print("hit")
        #print(self.display.text)
        value = int(self.display.text)
        dispvalue = int(self.displayDisp.text)
        Fantvalue = int(self.displayFant.text)
        self.displayFant.text = str(Fantvalue+3)
        Fantvalue += 3
        UserID_value = int(self.ids.userID_content_label.text)
        #print("User is " + self.ids.userID_content_label.text)
        self.display.text = str(value+1)
        self.displayDisp.text= str(dispvalue+1)
        kickvalue = value + 1
        dispvalue += 1
        con = sqlite3.connect('demo.db')    
        con.execute("UPDATE Users set Kicks =" + str(kickvalue) + " where UserID = " + str(UserID_value))
        con.execute("UPDATE Users set Disposals =" + str(dispvalue) + " where UserID = " + str(UserID_value))
        con.execute("UPDATE Users set Fantasy =" + str(Fantvalue) + " where UserID = " + str(UserID_value))
        con.commit()

    def add_oneHandball(self):
        #print("hit")
        #print(self.display.text)
        value = int(self.displayHandballs.text)
        dispvalue = int(self.displayDisp.text)
        Fantvalue = int(self.displayFant.text)
        self.displayFant.text = str(Fantvalue+2)
        Fantvalue += 2
        UserID_value = int(self.ids.userID_content_label.text)
        #print("User is " + self.ids.userID_content_label.text)
        self.displayHandballs.text = str(value+1)
        self.displayDisp.text= str(dispvalue+1)
        Handballvalue = value + 1
        dispvalue += 1
        con = sqlite3.connect('demo.db')    
        con.execute("UPDATE Users set Handballs =" + str(Handballvalue) + " where UserID = " + str(UserID_value))
        con.execute("UPDATE Users set Disposals =" + str(dispvalue) + " where UserID = " + str(UserID_value))
        con.execute("UPDATE Users set Fantasy =" + str(Fantvalue) + " where UserID = " + str(UserID_value))
        con.commit()

    def add_oneMark(self):
        #print("hit")
        #print(self.display.text)
        value = int(self.displayMarks.text)
        Fantvalue = int(self.displayFant.text)
        self.displayFant.text = str(Fantvalue+3)
        Fantvalue += 3
        UserID_value = int(self.ids.userID_content_label.text)
        #print("User is " + self.ids.userID_content_label.text)
        self.displayMarks.text = str(value+1)
        Markvalue = value + 1
        con = sqlite3.connect('demo.db')    
        con.execute("UPDATE Users set Marks =" + str(Markvalue) + " where UserID = " + str(UserID_value))
        con.execute("UPDATE Users set Fantasy =" + str(Fantvalue) + " where UserID = " + str(UserID_value))
        con.commit()

    def add_oneTackle(self):
        #print("hit")
        #print(self.display.text)
        value = int(self.displayTackles.text)
        Fantvalue = int(self.displayFant.text)
        self.displayFant.text = str(Fantvalue+4)
        Fantvalue += 4
        UserID_value = int(self.ids.userID_content_label.text)
        #print("User is " + self.ids.userID_content_label.text)
        self.displayTackles.text = str(value+1)
        Tacklesvalue = value + 1
        con = sqlite3.connect('demo.db')    
        con.execute("UPDATE Users set Tackles =" + str(Tacklesvalue) + " where UserID = " + str(UserID_value))
        con.execute("UPDATE Users set Fantasy =" + str(Fantvalue) + " where UserID = " + str(UserID_value))
        con.execute("UPDATE Users set Fantasy =" + str(Fantvalue) + " where UserID = " + str(UserID_value))
        con.commit()

    def add_oneClear(self):
        #print("hit")
        #print(self.display.text)
        value = int(self.displayClear.text)
        UserID_value = int(self.ids.userID_content_label.text)
        #print("User is " + self.ids.userID_content_label.text)
        self.displayClear.text = str(value+1)
        Clearvalue = value + 1
        con = sqlite3.connect('demo.db')    
        con.execute("UPDATE Users set Clearances =" + str(Clearvalue) + " where UserID = " + str(UserID_value))
        con.commit()

    def add_oneCont(self):
        #print("hit")
        #print(self.display.text)
        value = int(self.displayCont.text)
        UserID_value = int(self.ids.userID_content_label.text)
        #print("User is " + self.ids.userID_content_label.text)
        self.displayCont.text = str(value+1)
        Contvalue = value + 1
        con = sqlite3.connect('demo.db')    
        con.execute("UPDATE Users set Contested =" + str(Contvalue) + " where UserID = " + str(UserID_value))
        con.commit()

    def add_oneGoal(self):
        #print("hit")
        print(self.display.text)
        print(self.displayScore.text)
        value = float(self.displayScore.text)
        Fantvalue = int(self.displayFant.text)
        self.displayFant.text = str(Fantvalue+6)
        Fantvalue += 6
        UserID_value = int(self.ids.userID_content_label.text)
        #print("User is " + self.ids.userID_content_label.text)
        self.displayScore.text = str(value+1)
        Scorevalue = value + 1
        con = sqlite3.connect('demo.db')    
        con.execute("UPDATE Users set Score =" + str(Scorevalue) + " where UserID = " + str(UserID_value))
        con.execute("UPDATE Users set Fantasy =" + str(Fantvalue) + " where UserID = " + str(UserID_value))
        con.commit()

    def add_onePoint(self):
        #print("hit")
        #print(self.display.text)
        value = self.displayScore.text.split(".")
       
        Fantvalue = int(self.displayFant.text)
        self.displayFant.text = str(Fantvalue+1)
        Fantvalue += 1
        UserID_value = int(self.ids.userID_content_label.text)
        #print("User is " + self.ids.userID_content_label.text)
        value[1] = (int(value[1])) + 1
        self.displayScore.text = str(value[0]) + "." + str(value[1])
        Scorevalue = value[0] + "." + str(value[1])
        con = sqlite3.connect('demo.db')    
        con.execute("UPDATE Users set Score =" + str(Scorevalue) + " where UserID = " + str(UserID_value))
        con.execute("UPDATE Users set Fantasy =" + str(Fantvalue) + " where UserID = " + str(UserID_value))
        con.commit()

    def delete_player(self):
        UserID_value = int(self.ids.userID_content_label.text)
        print(UserID_value)
        con = sqlite3.connect('demo.db')    
        con.execute("DELETE from Users where UserID = " + str(UserID_value))
        con.commit()
        #self.MDApp = MDApp.get_running_app()
        #self.delete_player = self.MDApp.delete_player
    




class NScreen(Screen):
    
    def set_title(self):
        con = sqlite3.connect('demo.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM Users ORDER BY UserID ASC")
        table = cur.fetchall()
       
        for line in table:
            UserID, Username, Kicks, Handballs, Tackles, Clearances, Contested, GameDate, Vers, Score, Fantasy, Disposals, Marks, Jumper = line
            print("title is:" + Username)
            Disposals = Kicks + Marks
            Disposals = str(Disposals)
            Kicks = str(Kicks)
            Handballs = str(Handballs)
            Marks = str(Marks)
            Tackles = str(Tackles)
            Clearances = str(Clearances)
            Contested = str(Contested)
            Fantasy = str(Fantasy)
            Score = str(Score)
            Jumper = str(Jumper)
            
            print(Disposals)
            UserID =str(UserID)
            self.ids.card_box.add_widget(InfoCard(title=Username, GameDate_content=GameDate, kicks_content=Kicks, UserID_content=UserID, Handballs_content=Handballs, Marks_content=Marks, Tackles_content=Tackles, Clear_content=Clearances, Cont_content = Contested, Disp_content=Disposals, Fant_content=Fantasy, Score_content=Score, Jumper_content=Jumper))


    def refresh(self,ins):
            sm=Manager()
            self.sm.refresh()

    

class ScrManage(ScreenManager):
    def __init__(self):
        super(ScrManage, self).__init__()
        #base=Base('stats')
    def refresh(self):
            #self.current = value
            print("refresh")
            #self.current = 'home'
            #self.remove_widget(self.get_screen('stats'))
            #base=Base('stats')
            #self.add_widget(base)
            
            


class Sports(MDApp):
    dialog = None
    
    
    #sm.add_widget(HomeScreen(name='home'))
    #sm.add_widget(NScreen(name='stats'))

    #def remove_item(self, instance):
        #self.screen.ids.InfoCard.remove_widget(instance)
   
    def build(self):
        self.sm = ScrManage()
        return Builder.load_string(kv)

    def callback_for_menu_items(self, *args):
        print(args[0])

    def show_example_custom_bottom_sheet(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
        
        self.custom_sheet.open()
        

    def showAddPlayer_Dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Add Player:",
                type="custom",
                content_cls=AddPlayerContent(),
                size_hint=[.8, .8],
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.on_cancel
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.on_save
                    ),
                ],
            )
        self.dialog.open()

    def on_save(self, obj):
        print("save")
        sqliteConnection = sqlite3.connect('demo.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        PlayerName = self.dialog.content_cls.ids.playerNametxt.text
        game_date = self.dialog.content_cls.ids.date_picker_label.text
        against = self.dialog.content_cls.ids.Againsttxt.text
        gurnsey = self.dialog.content_cls.ids.SliderJumpertxt.text
        sqlite_insert_query = """INSERT INTO users
                          (Username, GameDate, Vers, Jumper) 
                           VALUES 
                          (?, ?, ?, ?)"""

        count = cursor.execute("INSERT INTO users (Username, GameDate, Vers, Jumper) VALUES (?, ?, ?, ?)", (PlayerName, game_date, against, gurnsey))
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()
        #sm = ScreenManager()
        print(self.sm.screen_names)
        #self.sm.remove_widget(self.sm.get_screen('stats'))
        #ScreenManager.remove_widget(ScreenManager.get_screen('stats'))
        
        self.dialog.dismiss()

    def show_alert_dialog(self):

        self.dialog = MDDialog(
            text="Delete Player?",
            size_hint=[.8, .8],
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="DELETE", text_color=self.theme_cls.primary_color,
                ),
            ],
        )
        self.dialog.open() 

    def close_dialog(self, obj):
        self.dialog.dismiss()
        
    
        
        
    

    def on_cancel(self, obj):
        self.dialog.dismiss()

    


Sports().run()
