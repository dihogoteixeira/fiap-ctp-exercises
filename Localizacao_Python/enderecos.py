from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo'
resultado = Geocoder('AIzaSyCIf7vpbvpveAqUmbd9_jUze-yU1x85rdY').geocode(endereco)
reverse = Geocoder('AIzaSyCIf7vpbvpveAqUmbd9_jUze-yU1x85rdY').reverse_geocode(-23.5703022,-46.6451267)
print(resultado)