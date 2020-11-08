class computer(object):
	def __init__(self,brand,ram,harddisk,processor):
		self.brand =brand;
		self.ram = ram;
		self.hdsisk = harddisk;
		self.processor = processor;



c1 = computer("hp","16g","500g","i5");

print(c1);

setattr(c1,"ram","8g");

print(getattr(c1,"ram"));

print(hasattr(c1,"floppy"));
print(hasattr(c1,"ram"));

del c1

