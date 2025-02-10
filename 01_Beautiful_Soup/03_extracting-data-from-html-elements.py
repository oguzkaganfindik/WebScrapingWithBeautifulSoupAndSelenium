#######################################
# Extracting Data from HTML Elements
#######################################

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Animal Table</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px;
    }

    th, td {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }

    th {
      background-color: #f2f2f2;
    }

    img {
object-fit: cover;
      max-width: 50px;
      max-height: 50px;
    }
  </style>
</head>
<body>

  <h2>Animal Table</h2>

  <table>
    <thead><tr>
      <th>Image</th>
      <th>Animal</th>
      <th>Description</th>
      <th>Nickname</th>
    </tr></thead>
    <tbody>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Lion"></td>
      <td><a href="https://en.wikipedia.org/wiki/Lion" target="_blank">Lion</a></td>
      <td>The lion is a large carnivorous mammal. It is known for its majestic appearance and is often referred to as the "king of the jungle."</td>
      <td> Majestic<br>King  </td>
    </tr>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1551316679-9c6ae9dec224?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Elephant"></td>
      <td><a href="https://en.wikipedia.org/wiki/Elephant" target="_blank">Elephant</a></td>
      <td>Elephants are the largest land animals. They are known for their long trunks and large ears.</td>
      <td> Trunked<br>  Giant</td>
    </tr>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1570481662006-a3a1374699e8?q=80&w=1965&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Dolphin"></td>
      <td><a href="https://en.wikipedia.org/wiki/Dolphin" target="_blank">Dolphin</a></td>
      <td>Dolphins are highly intelligent marine mammals known for their playful behavior and communication skills.</td>
      <td> Playful<br>Communicator</td>
    </tr>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1599631438215-75bc2640feb8?q=80&w=2127&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Butterfly"></td>
      <td><a href="https://en.wikipedia.org/wiki/Butterfly" target="_blank">Butterfly</a></td>
      <td>Butterflies are beautiful insects with colorful wings. They undergo a process called metamorphosis from caterpillar to butterfly.</td>
      <td> Colorful<br>Metamorphosis</td>
    </tr>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1552633832-4f5a1b110980?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Penguin"></td>
      <td><a href="https://en.wikipedia.org/wiki/Penguin" target="_blank">Penguin</a></td>
      <td>Penguins are flightless birds that are well-adapted to life in the water. They are known for their tuxedo-like black and white plumage.</td>
      <td> Tuxedoed     <br>Adaptation  </td>
    </tr>
  </tbody>
  </table>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

tbody_tag = soup.find("tbody")
tr_tag_list = tbody_tag.find_all("tr")
print(tr_tag_list)

tr_tag = tr_tag_list[0]
tr_tag

img_tag = tr_tag.find("img")
a_tag = tr_tag.find("a")

nickname_td = tr_tag.find_all("td")[-1]
desc_td = tr_tag.find_all("td")[-2]
desc_td.text

nickname_td
nickname_td.text
nickname_td.get_text(separator=" ", strip=True)

img_tag

alt_attribute = img_tag["alt"]
alt_attribute

src_attribute = img_tag["src"]
src_attribute

a_tag
a_tag["href"]
a_tag["target"]
