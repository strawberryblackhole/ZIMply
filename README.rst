**ZIMply** is an easy to use, offline reader for `Wikipedia <https://www.wikipedia.org>`__ which provides access to the offline `Wikipedia <https://www.wikipedia.org>`__ through any ordinary browser. **ZIMply** is written entirely in `Python <https://www.python.org>`__ and, as the name implies, relies on `ZIM files <http://www.openzim.org/wiki/OpenZIM>`__. Each ZIM file is a bundle containing thousands of articles, images, etc. as found on websites such as `Wikipedia <https://www.wikipedia.org>`__. The format is made popular by `Kiwix <http://www.kiwix.org>`__, which is a program to read such files offline on your device. As indicated, **ZIMply** differs from `Kiwix <http://www.kiwix.org>`__ in that it provides access through the browser. It accomplishes this by running its own HTTP server. This furthermore makes it easy to install **ZIMply** on one device (a *server*, such as a `Raspberry Pi <https://www.raspberrypi.org/products/>`__) and access it on others (the *clients*).

**ZIMply** depends on the `mako <http://www.makotemplates.org>`__ (for templating) and `whoosh <https://pypi.python.org/pypi/Whoosh/>`__ (for indexing) packages. The easiest way to install these dependencies is by using:

.. code:: bash

    pip install mako
    pip install whoosh

When you have both Python 2.* and Python 3.* installed on your system, you may need to replace `pip` with `pip3` depending on your setup.

**ZIMply** can be used as-is and does not require any configuration out of the box. It suffices to delete the `wiki.zim` file and replace it with your ZIM file of choice which you rename to `wiki.zim` (and delete the index.idx if it has already been created). A large collection of ZIM files is available from http://download.kiwix.org/zim/ . If you run **ZIMply** on your local system, you can access it by visiting http://localhost:9454 - spelling out as :WIKI on a keypad. To access **ZIMply** from another system, you need to know the IP address of the system that is running **ZIMply**. You can then easily access it by visiting http://ip_address:9454 where you replace ip_address with the actual IP address.

To modify the standard parameters, or use **ZIMply** in your own project, you need to modify or delete the last rule in `zimply.py` which is used to start the server. **ZIMply** comes with a very permissive license, so you can do whatever you want with the source code as long as you keep the copyright notice intact.