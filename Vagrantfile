#Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "blog"

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 2
  end

  config.ssh.insert_key = false
  config.ssh.forward_agent = true
  # config.vm.synced_folder ".", "/vagrant", type: "nfs"
  config.vm.network "private_network", ip: "172.28.128.100"
end
