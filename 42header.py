import os
import sys
from datetime import datetime

# Configuration
USERNAME = "your42login"
EMAIL = f"{USERNAME}@student.42.fr"

HEADER_TEMPLATE = """\
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   {filename:<46}                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: {username:<38}                             +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: {created:<30}                            #+#    #+#             */
/*   Updated: {updated:<30}                           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

"""

def generate_header(filename):
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    header = HEADER_TEMPLATE.format(
        filename=filename,
        username=f"{USERNAME} <{EMAIL}>",
        created=now + f" by {USERNAME}",
        updated=now + f" by {USERNAME}"
    )
    return header

def main():
    if len(sys.argv) < 2:
        print("Usage: 42header <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist.")
        sys.exit(1)

    header = generate_header(os.path.basename(filename))

    with open(filename, "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(header + content)

    print(f"Header added to {filename}")

if __name__ == "__main__":
    main()
