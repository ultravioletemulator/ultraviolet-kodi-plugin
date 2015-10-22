__author__ = 'developer'

import ultraviol.configuration as config
import ultraviol.apputils as utils
import libtorrent as lt
import bencode
import hashlib
import base64

import time

TORRENT_PORT1=6881
TORRENT_PORT2=6891

def downloadMagnet (magnet):
    print ("download magnet")
    # http://stackoverflow.com/questions/8689828/libtorrent-given-a-magnet-link-how-do-you-generate-a-torrent-file
    #http://stackoverflow.com/questions/10251305/torrent-info-and-magnet-links-in-libtorrent-python-bindings


def downloadTorrent (torrent ):
    torrent="test.torrent"


    ses = lt.session()
    ses.listen_on(TORRENT_PORT1, TORRENT_PORT2)

    e = lt.bdecode(open(torrent, 'rb').read())
    info = lt.torrent_info(e)

    params = { "save_path": '.', \
               "storage_mode": lt.storage_mode_t.storage_mode_sparse, \
               "ti": info }
    h = ses.add_torrent(params)

    s = h.status()
    while (not s.is_seeding):
        s = h.status()

        state_str = ['queued', 'checking', 'downloading metadata', \
                     'downloading', 'finished', 'seeding', 'allocating']
        print( '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
               s.num_peers, state_str[s.state]))

        time.sleep(1)


def generateTorrentOfFile (file):
    print("generateTorrentOfdownloaded Files for sharing...")
    # http://www.libtorrent.org/reference-Create_Torrents.html
    # downloadedFolder = utils.getHomeFolder()+"/"+config.DOWNLOAD_FOLDER
    from os import listdir

    print (file)
    fs = lt.file_storage()
    # file_storage fs;

    # // recursively adds files in directories
    # add_files(fs, "./my_torrent");
    lt.add_files(fs, file)
    t = lt.create_torrent() # ?¿?¿?¿?¿?¿?¿?¿?¿¿?¿¿?
    # create_torrent t(fs);
    lt.create_torrent(t, fs)

    t.add_tracker("http://my.tracker.com/announce");
    t.set_creator("Ultraviolet test");

    # // reads the files and calculates the hashes
    # set_piece_hashes(t, ".");
    lt.set_piece_hashes(t,".")
    # ofstream out("my_torrent.torrent", std::ios_base::binary);
    # bencode(std::ostream_iterator<char>(out), t.generate());
    fileContent = t.generate()
    # byteContent= bytearray(fileContent)
    # newFile = open (utils.getHomeFolder()+"torrents/newTorrnet.torrent", "wb")
    # newFile.write(byteContent)
    writeBinaryFile(utils.getHomeFolder()+"torrents/newTorrnet.torrent", fileContent)


def generateTorrentOfdownloadedFiles(downloadedFolder):
    print("generateTorrentOfdownloaded Files for sharing...")
    # http://www.libtorrent.org/reference-Create_Torrents.html
    # downloadedFolder = utils.getHomeFolder()+"/"+config.DOWNLOAD_FOLDER
    from os import listdir
    for file in listdir (downloadedFolder):
        print (file)
        fs = lt.file_storage()
        # file_storage fs;

        # // recursively adds files in directories
        # add_files(fs, "./my_torrent");
        lt.add_files(fs, downloadedFolder)
        t = lt.create_torrent() # ?¿?¿?¿?¿?¿?¿?¿?¿¿?¿¿?
        # create_torrent t(fs);
        lt.create_torrent(t, fs)

        t.add_tracker("http://my.tracker.com/announce");
        t.set_creator("Ultraviolet test");


        # // reads the files and calculates the hashes
        # set_piece_hashes(t, ".");
        lt.set_piece_hashes(t,".")
        # ofstream out("my_torrent.torrent", std::ios_base::binary);
        # bencode(std::ostream_iterator<char>(out), t.generate());
        fileContent = t.generate()
        # byteContent= bytearray(fileContent)
        # newFile = open (utils.getHomeFolder()+"torrents/newTorrnet.torrent", "wb")
        # newFile.write(byteContent)
        writeBinaryFile(utils.getHomeFolder()+"torrents/newTorrnet.torrent", fileContent)


def generateMagnetFromTorrent(torrentFile):
    print("generateMagnetFromTorrent")
    # http://stackoverflow.com/questions/12479570/given-a-torrent-file-how-do-i-generate-a-magnet-link-in-python

    torrent = open(torrentFile, 'r').read()
    metadata = bencode.bdecode(torrent)
    hashcontents = bencode.bencode(metadata['info'])
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest)
    params = {'xt': 'urn:btih:%s' % b32hash,
            'dn': metadata['info']['name'],
            'tr': metadata['announce'],
            'xl': metadata['info']['length']}
    import urllib
    paramstr = urllib.urlencode(params)
    magneturi = 'magnet:?%s' % paramstr
    print ("MagnetLink: %s" % (magneturi))


def generateTorrentFromMagnet (magnet):
    print("generateTorrentFromMagnet")
    # file_storage fs;
    #
    # // recursively adds files in directories
    # add_files(fs, "./my_torrent");
    #
    # create_torrent t(fs);
    # torrent_info ti = handle.get_torrent_info()
    handle = lt.torrent_handle()
    ti = handle.get_torrent_info()

    t = lt.create_torrent() # ?¿?¿?¿?¿?¿?
    lt.create_torrent (t, ti)

    t.add_tracker("http://my.tracker.com/announce");
    t.set_creator("Ultraviolet test");

    # // reads the files and calculates the hashes
    pieceHashes = lt.set_piece_hashes(t,".")
    # set_piece_hashes(t, ".");
    writeBinaryFile("tmp.torrent",t.generate())



def writeBinaryFile (name, content):
    byteContent= bytearray(content)
    newFile = open (utils.getHomeFolder()+"torrents/"+name, "wb")
    newFile.write(byteContent)

