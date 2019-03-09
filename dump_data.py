from models.register import Sound
import mlab
mlab.connect()

sound_test1 = Sound(name="quatgio", link="https://www.dropbox.com/s/6i0gfzffmy06nld/ti%E1%BA%BFng%20qu%E1%BA%A1t%20gi%C3%B3%20%28mp3cut.net%29.mp3?raw=1")
sound_test2 = Sound(name="samchop", link="https://www.dropbox.com/s/fko1x8r7ifslkh9/ti%E1%BA%BFng%20s%E1%BA%A5m%20ch%E1%BB%9Bp%20%28mp3cut.net%29.mp3?raw=1")
sound_test3 = Sound(name="giotnuoc", link="https://www.dropbox.com/s/vi0d8sbmmfleb08/ti%E1%BA%BFng%20gi%E1%BB%8Dt%20n%C6%B0%E1%BB%9Bc%20%28mp3cut.net%29.mp3?raw=1")
sound_test4 = Sound(name="giothoi", link="https://www.dropbox.com/s/j1k16hyedrlbgpx/ti%E1%BA%BFng%20gi%C3%B3%20th%E1%BB%95i%20%28mp3cut.net%29.mp3?raw=1")
sound_test5 = Sound(name="contrung", link="https://www.dropbox.com/s/rkx4ho9gtncersn/ti%E1%BA%BFng%20c%C3%B4n%20tr%C3%B9ng%20%28mp3cut.net%29.mp3?raw=1")
sound_test6 = Sound(name="beplua", link="https://www.dropbox.com/s/loydn20mfg82ry6/ti%E1%BA%BFng%20b%E1%BA%BFp%20l%E1%BB%ADa%20ch%C3%A1y%20%28mp3cut.net%29.mp3?raw=1")
sound_test1.save()
sound_test2.save()
sound_test3.save()
sound_test4.save()
sound_test5.save()
sound_test6.save()

