from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

# counter integer
image = 1

class YourApp(App):

    # methods for previous
    def previous(self, instance):
        #link to our image variable - global, and subtract 1
        global image
        image = image - 1

        # check to see if image is <= 0
        if image <= 0:
            image = 7

        #if check for numbers 1 through 7
        if image == 1:
            self.img.source = 'one.png'
        elif image == 2:
            self.img.source = 'two.png'
        elif image == 3:
            self.img.source = 'three.png'
        elif image == 4:
            self.img.source = 'four.png'
        elif image == 5:
            self.img.source = 'five.png'
        elif image == 6:
            self.img.source = 'six.png'
        elif image == 7:
            self.img.source = 'seven.png'



    # method for next
    def next(self, instance):
        #link to our image variable - global, and add 1
        global image
        image = image + 1

        # check to see if image is >= 7
        if image > 7:
            image = 1

        #if check for numbers 1 through 7
        if image == 1:
            self.img.source = 'one.png'
        elif image == 2:
            self.img.source = 'two.png'
        elif image == 3:
            self.img.source = 'three.png'
        elif image == 4:
            self.img.source = 'four.png'
        elif image == 5:
            self.img.source = 'five.png'
        elif image == 6:
            self.img.source = 'six.png'
        elif image == 7:
            self.img.source = 'seven.png'


    def build(self):

        # create our layout for the box buttons
        buttonBox = BoxLayout(orientation='horizontal', pos_hint={'center_x':.75})

        # our overal box layout container
        layout = BoxLayout(orientation='vertical', pos_hint={'center_x':.5})

        # create button one
        b1 = Button(text='Previous', size=(200, 100), size_hint=(None, None))
        # link/bind this to the correct method
        b1.bind(on_press=self.previous)

        # create button two
        b2 = Button(text="Next", size=(200, 100), size_hint=(None, None))
        # link/bind this to correct method
        b2.bind(on_press=self.next)

        # add buttons to the button box
        buttonBox.add_widget(b1)
        buttonBox.add_widget(b2)

        # load our first image
        self.img = Image(source ='one.png')

        # add image to the overall layout box
        layout.add_widget(self.img)

        # add buttonBox to the overall layout box
        layout.add_widget(buttonBox)

        return layout

YourApp().run()
