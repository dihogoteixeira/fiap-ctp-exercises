from pygeocoder import Geocoder

endereco = '348, Rua Líra Cearense, São Paulo, SP'
print(Geocoder('AIzaSyCIf7vpbvpveAqUmbd9_jUze-yU1x85rdY').geocode(endereco).coordinates)