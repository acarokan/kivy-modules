menu = Menu()

<h1> switch_sizable fonksiyonu <h1>

Menu açık durumda olduğunda boyutlarını belirlememizi sağlar.
Eğer size_hint_x girildiyse width'in bir etkisi olmaz.
Eğer size_hint_y girildiyse height değerinin bir etkisi olmaz.
size_hint değerlerinin None olmasını istersek "None" şeklinde girmeliyiz.

menu.switch_sizable(size_hint_x,size_hint_y,width,height)

<h1> set_background_color fonksiyonu <h1>

Element yerleşimlerinin olduğu BoxLayout'un arkaplan rengini değiştirir.
Parametreler sırası ile rgba formatında girilir.

menu.set_background_color(r,g,b,a)

<h1> set_background_image fonksinu  <h1>

Element yerleşimlerinin olduğu BoxLayout'a bir arkaplan resmi atar.
Parametre olarak resim dosyasının yolunu String olarak alır.

menu.set_background_image("path/file")

<h1> set_header_background_color fonksiyonu <h1>

Header kısmının arkaplan rengini ayarlamak için kullanılır.
Parametreler sırası ile rgba formatında girilir.

menu.set_header_background_color(r,g,b,a)

<h1> set_header_background_image <h1>

Header kısmının arkaplan resmini ayarlamak için kullanılır.
Parametre olarak resim dosyasının yolunu String olarak alır.

menu.set_header_background_image("path/file")

<h1> set_header_image fonksiyonu <h1>

Header kısmında profil avatarının bulundu yer için bir resim belirler.
Parametre olarak resim dosyasının yolunu String olarak alır.

menu.set_header_image("path/file")

<h1> set_header_text fonksiyonu <h1>

Header kısmındaki text'i değiştirir.
Parametre olarak istenen text String olarak girilir.

menu.set_header_text("header text")

<h1> add_element fonksiyonu <h1>

Menuye Button elementleri eklememizi sağlar.
Butonlar girilen sıraya göre sıralanır.
Parametre olarak buton ismi ve butonda yazacak text Parametrelerini String olarak alır.
Buton isimleri benzersiz olmalıdır. Daha sonraki kullanımlarda bu özellikten yararlanılır.

menu.add_element("element_name","element_text")

<h1> get_element_list fonksiyonu <h1>

Menudeki tüm elementleri bir dict olarak döndürür.

element_list = manu.get_element_list()
element_list["element_name"].bind(on_press = a_function)