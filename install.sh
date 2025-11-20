#!/bin/bash

# erdamn test o yea

INSTALL_DIR="$HOME/dexioz"
SYMLINK="/usr/local/bin/dexioz"

if [ "$1" == "-u" ]; then
    # Uninstall kısmı
    if [ -L "$SYMLINK" ]; then
        sudo rm "$SYMLINK"
        echo "Dexioz terminal kısayolu kaldırıldı."
    else
        echo "Dexioz terminal kısayolu bulunamadı."
    fi

    if [ -d "$INSTALL_DIR" ]; then
        read -p "Dexioz klasörünü de silmek ister misin? (y/n): " yn
        case $yn in
            [Yy]* ) rm -rf "$INSTALL_DIR"; echo "Dexioz klasörü silindi!";;
            * ) echo "Dexioz klasörü bırakıldı.";;
        esac
    fi
    exit 0
fi

# Normal install kısmı
if [ ! -d "$INSTALL_DIR" ]; then
    echo "Dexioz klasörü $INSTALL_DIR bulunamadı. Lütfen proje klasörünü $HOME dizinine taşı."
    exit 1
fi

chmod +x "$INSTALL_DIR/dexioz.py"
sudo ln -sf "$INSTALL_DIR/dexioz.py" "$SYMLINK"

echo "Dexioz kuruldu. Artık terminalden 'dexioz' yazarak çalıştırabilirsin."
