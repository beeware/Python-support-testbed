###########################################################################
# Linux specific tests
###########################################################################
import os
import sys

from .utils import assert_


def exit(failures):
    sys.exit(failures)


def test_dbm_gdbm():
    "The GNU DBM module has been compiled and works"
    from dbm import gnu as gdbm
    import tempfile

    cache_name = f'{tempfile.mkdtemp()}/gdbm'
    with gdbm.open(cache_name, 'c') as db:
        db['hello'] = 'world'

        assert_(db['hello'] == b'world')


def test_glib():
    "Glib is available"
    import gi
    gi.require_version('GLib', '2.0')
    from gi.repository import GLib

    assert GLib.base64_encode(b"hello world") == "aGVsbG8gd29ybGQ="


def test_pango():
    "Pango is available"
    import gi
    gi.require_version('Pango', '1.0')
    from gi.repository import Pango

    font = Pango.FontDescription()
    font.set_family("Cantarell")
    font.set_size(16 * Pango.SCALE)
    font.set_weight(Pango.Weight.BOLD)
    assert_(font.to_string() == "Cantarell Bold 16")


def test_gdk():
    "GDK is available"
    import gi
    gi.require_version('Gdk', '3.0')
    from gi.repository import Gdk

    color = Gdk.Color(37, 42, 69)
    assert_(color.to_string() == "#0025002a0045")


def test_gtk():
    "GTK is available"
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk

    app = Gtk.Application()
    assert_(app.get_windows() == [])


def test_gdkpixbuf():
    "GDKPixbuf is available"
    import gi
    gi.require_version('GdkPixbuf', '2.0')
    from gi.repository import GdkPixbuf

    pixbuf = GdkPixbuf.Pixbuf.new_from_file(
        os.path.join(
            os.path.dirname(__file__),
            "resources",
            "test-pattern.png"
        )
    )
    assert_(pixbuf.get_height() == 768)


def test_cairo():
    "Cairo is available"
    import cairo

    surface = cairo.ImageSurface(cairo.Format.ARGB32, 100, 200)
    assert_(surface.get_width() == 100)


def test_pillow():
    "Pillow can be used to load images"
    from PIL import Image

    for extension in ['png', 'jpg']:
        image = Image.open(
            os.path.join(
                os.path.dirname(__file__),
                "resources",
                f"test-pattern.{extension}"
            )
        )
        assert_(image.size == (1366, 768))
