import esp32
import micropython
a = esp32.idf_heap_info(esp32.HEAP_DATA)
print(a)
print(micropython.mem_info())