from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>HumanAIx</title>
    <meta name="description" content="HumanAIx Landing Page" />
    <meta name="keywords" content="artificial intelligence, human-AI interaction, innovative projects" />
    <meta name="author" content="HumanAIx" />
    <link rel="stylesheet" href="https://unpkg.com/tailwindcss@2.2.19/dist/tailwind.min.css" />
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700" rel="stylesheet" />
    <link rel="stylesheet" href="style.css" />
  </head>
  <body class="text-white gradient" style="font-family: 'Source Sans Pro', sans-serif;">
    <nav id="header" class="fixed w-full">
      <div class="container mx-auto py-2">
        <div>
          <img src="Logo.png" alt="Logo" class="h-16 inline" />
        </div>
      </div>
    </nav>
    <div class="pt-24">
      <div class="container px-3 mx-auto">
        <div class="w-full">
          <h1 class="my-4 text-5xl font-bold">AI made Human</h1>
          <p class="text-2xl">Our mission is to improve the interaction between humans and artificial intelligence. We are developing several innovative projects that we'll be unveiling soon. Keep an eye out for updates, and be the first to learn about our progress.</p>
          <input
            type="text"
            class="
              inline-block mt-3
              form-control
              px-3
              py-1.5
              text-base
              font-normal
              text-gray-700
              bg-white bg-clip-padding
              border border-solid border-gray-100
              rounded
              transition
              ease-in-out
              focus:text-gray-700 focus:bg-white focus:border-blue-300 focus:outline-none 
              w-1/2 sm:w-1/4
              "
            id="emaillistFormInput"
            placeholder="Join our mailing list and stay in the loop"
          />
          <video width="320" height="240" controls class="mt-3 py-1.5">
            <source src="Sofia.mp4" type="video/mp4">
          </video>
        </div>
      </div>
    </div>
  </body>
</html>
"""

if __name__ == "__main__":
    app.run()
