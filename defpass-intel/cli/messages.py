from functools import reduce
from cli.colors import Colors

def sum_pages(intels):
    return reduce(lambda total, intel: total + len(intel.pages), intels, 0)

def get_intels_source(intels):
    return " ".join(list(map(lambda intel: "\n- " + intel.source, intels)))

def sum_intel_content(intel):
    return "\n".join(map(lambda page: f"Page: {Colors.GRAY} {page[:256].strip("\n")} {Colors.RESET}", intel.pages))
 
Messages = {
    "repository.read_repository": lambda classname: f"{Colors.GREEN}+ Read {Colors.RESET}{Colors.CYAN}{Colors.BOLD}{classname}{Colors.RESET} from intel repository",
    "repository.save_repository": lambda classname: f"{Colors.GREEN}+ Saved {Colors.RESET}{Colors.CYAN}{Colors.BOLD}{classname}{Colors.RESET} to intel repository",
    "collector.connected": lambda base_url: f"{Colors.CYAN} {Colors.BOLD}Connected{Colors.RESET} to {base_url}",
    "collector.collected": lambda params: f"{Colors.GREEN} {Colors.BOLD}+ Collected {Colors.RESET} {sum_pages(params['intels'])} pages from {get_intels_source(params['intels'])}",
    "intel.progress": lambda params: f"{Colors.GREEN} {Colors.BOLD}[{params['count']}/{params['all']}]{Colors.RESET} collected from {Colors.BOLD}{params['intel'].source}{Colors.RESET}{Colors.BOLD}{Colors.CYAN}\nPreview:\n{Colors.RESET}{sum_intel_content(params['intel'])}\n"
}