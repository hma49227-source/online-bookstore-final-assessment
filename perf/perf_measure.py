import timeit
import cProfile
import pstats
from models import Book, Cart

def setup_cart(n=100):
    cart = Cart()
    books = [Book(f"Title{i}", "Fiction", i+1.0, "") for i in range(n)]
    for b in books:
        cart.add_book(b)
    return cart

def measure_timeit():
    stmt = "cart.add_book(Book('X', 'Fiction', 1.0, ''))"
    setup = "from models import Book, Cart; cart=Cart()"
    t = timeit.timeit(stmt, setup=setup, number=1000)
    print(f"timeit: adding 1000 items took {t:.6f}s")

def measure_cprofile():
    cart = setup_cart(200)
    profiler = cProfile.Profile()
    profiler.enable()
    for _ in range(100):
        for title, item in list(cart.items.items()):
            cart.update_quantity(title, item.quantity + 1)
        total = cart.total_price()
    profiler.disable()
    ps = pstats.Stats(profiler).sort_stats('cumtime')
    ps.print_stats(20)

if __name__ == "__main__":
    print("== timeit measurement ==")
    measure_timeit()
    print("\n== cProfile measurement ==")
    measure_cprofile()
