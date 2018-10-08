#include "optparse.h"
#include <iostream>
#include <string>

int main(int argc, char **argv)
{
	optparse::OptionParser parser = optparse::OptionParser().description("FrankenFuzzer");
    //parser.add_option("-f", "--file").dest("filename").help("write report to FILE").metavar("FILE");
   // parser.add_option("-q", "--quiet").action("store_false").dest("verbose").set_default("1").help("don't print status messages to stdout");
    const optparse::Values options = parser.parse_args(argc, argv);
    const std::vector<std::string> args = parser.args();

    if (options.get("verbose"))
    {
        std::cout << options["filename"] << "\n";
    }
	
	return 0;
}
