# Fonte: adaptado de https://refactoring.guru/pt-br/design-patterns/facade

# Essas são algumas das classes de um framework complexo de um
# conversor de vídeo de terceiros. Nós não controlamos aquele
# código, portanto não podemos simplificá-lo.

class VideoFile:
    pass
# ...

class VP9CompressionCodec:
    pass
# ...

class MPEG4CompressionCodec:
    pass
# ...

class CodecFactory:
    pass
# ...

class BitrateReader:
    pass
# ...

class AudioMixer:
    pass
# ...

# Nós criamos uma classe fachada para esconder a complexidade do framework atrás de uma interface simples.
# É uma troca entre funcionalidade e simplicidade.
class VideoConverter:
    def convert(filename, format):
        file = VideoFile(filename)
        sourceCodec =  CodecFactory().extract(file)
        if (format == "mp4"):
            destinationCodec = MPEG4CompressionCodec()
        else:
            destinationCodec = VP9CompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = AudioMixer().fix(result)
        return result
        
# As classes da aplicação não dependem de um bilhão de classes # fornecidas por um framework complexo. 
# Também, se você decidir  trocar de frameworks, você só precisa reescrever a classe Facade.
class Application:
    def main():
        conversor = VideoConverter()
        mp4 = conversor.convert("funny-cats-video.mp4", "mp4")
        mp4.save()