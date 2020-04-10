# ...
exec { 'Puppet HTTP':
command => "sudo apt-get update && sudo apt-get -y install nginx && sudo mkdir -p /data/ && sudo mkdir -p /data/web_static/ && sudo mkdir -p /data/web_static/releases/ && sudo mkdir -p /data/web_static/shared/ && sudo mkdir -p /data/web_static/releases/test/ && echo  'Holberton School' | sudo tee /data/web_static/releases/test/index.html && sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && sudo chown -R ubuntu:ubuntu /data/ && sudo sed -i '45 a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default && sudo service nginx restart",
provider => 'shell',
}
