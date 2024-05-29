# Weather in README
Updates your README.md file with the weather of a city

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bumb7ebee/weather-profile-actions/main/assets/screenshot/partial-dark.png"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/bumb7ebee/weather-profile-actions/main/assets/screenshot/partial-light.png"/>
  <img title="Screenshot" alt="Screenshot" src="https://raw.githubusercontent.com/bumb7ebee/weather-profile-actions/main/assets/screenshot/partial-light.png"/>
</picture>

## How to use?
1. Star this repo 😉
2. Obtain an API key from [OpenWeather](https://openweathermap.org/)
3. Go to your repository
4. Go to your repository's `Settings`
5. Add a new repository secret named `WEATHER_API_KEY` containing your API key for `Actions` in `Secrets and variables`
6. Add the following section to your README.md file. The workflow will replace this comment with the weather:
```markdown
<!-- WEATHER:START -->
<!-- WEATHER:END -->
```
7. Create a folder named `.github` and create a `workflows` folder inside it, if it doesn't exist.
8. Create a new file named `weather-profile-workflow.yml` with the following contents inside the workflows folder:
```yml
name: Update Weather
on:
  schedule: # run workflow automatically
    - cron: '0 */3 * * *' # runs every three hours
  # allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
permissions:
  contents: write # to write the generated contents to the README
jobs:
  build:
    name: Update this repo's README with recent weather
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Pull in weather data
        uses: bumb7ebee/weather-profile-actions@v1.0.0
        with:
          weather-api-key: ${{ secrets.WEATHER_API_KEY }} # secret variable of OpenWeather API KEY
          city-id: 740483 # city id obtained from OpenWeather
          units: c # centigrade (c) or fahrenheit (f)
          country-code: tr # country code obtained from https://flagicons.lipis.dev/
          readme-path: README.md # relative path of the README file. something like: README, README.md, src/README, src/README.md, etc.
```
9. Wait for it to run automatically, or you can also trigger it manually to see the result instantly.
