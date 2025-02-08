import pulp
import ipywidgets as widgets
from IPython.display import display

# Definicja funkcji optymalizacji produkcji batonów
def optimize_production(price_mars, price_snickers, max_chocolate, max_caramel, max_sugar, max_oil, max_nuts, 
                        choco_mars, caramel_mars, sugar_mars, oil_mars, 
                        choco_snickers, nuts_snickers, caramel_snickers, oil_snickers):
    
    # 1. Tworzenie problemu liniowego - Maksymalizacja zysków
    problem = pulp.LpProblem("Optymalizacja_produkcji_batonow", pulp.LpMaximize)

    # 2. Zmienne decyzyjne: ile kilogramów Marsów i Snickersów produkować
    mars = pulp.LpVariable('Mars', lowBound=0, cat='Continuous')
    snickers = pulp.LpVariable('Snickers', lowBound=0, cat='Continuous')

    # 3. Funkcja celu: Maksymalizacja przychodu
    problem += price_mars * mars + price_snickers * snickers, "Całkowity zysk"

    # 4. Ograniczenia zasobów
    problem += choco_mars * mars + choco_snickers * snickers <= max_chocolate, "Zasoby_czekolady"
    problem += caramel_mars * mars + caramel_snickers * snickers <= max_caramel, "Zasoby_karmelu"
    problem += sugar_mars * mars <= max_sugar, "Zasoby_cukru"
    problem += oil_mars * mars + oil_snickers * snickers <= max_oil, "Zasoby_oleju"
    problem += nuts_snickers * snickers <= max_nuts, "Zasoby_orzechow"

    # 5. Rozwiązywanie problemu
    problem.solve()

    # 6. Wyświetlenie wyniku
    print(f"Status rozwiązania: {pulp.LpStatus[problem.status]}")
    print(f"Produkuj {mars.varValue:.2f} kg Marsów dziennie")
    print(f"Produkuj {snickers.varValue:.2f} kg Snickersów dziennie")
    print(f"Całkowity zysk: {pulp.value(problem.objective):.2f} zł")

# Slidery do dynamicznej zmiany parametrów
price_mars_slider = widgets.FloatSlider(value=100, min=50, max=150, step=1, description='Cena Mars [zł/kg]')
price_snickers_slider = widgets.FloatSlider(value=105, min=50, max=150, step=1, description='Cena Snickers [zł/kg]')

max_chocolate_slider = widgets.FloatSlider(value=6000, min=1000, max=10000, step=100, description='Max Czekolada [kg]')
max_caramel_slider = widgets.FloatSlider(value=2500, min=500, max=5000, step=100, description='Max Karmel [kg]')
max_sugar_slider = widgets.FloatSlider(value=1500, min=500, max=3000, step=100, description='Max Cukier [kg]')
max_oil_slider = widgets.FloatSlider(value=500, min=100, max=1000, step=10, description='Max Olej [kg]')
max_nuts_slider = widgets.FloatSlider(value=2000, min=500, max=3000, step=100, description='Max Orzechy [kg]')

choco_mars_slider = widgets.FloatSlider(value=0.5, min=0, max=1, step=0.01, description='Czekolada w Mars [kg]')
caramel_mars_slider = widgets.FloatSlider(value=0.2, min=0, max=1, step=0.01, description='Karmel w Mars [kg]')
sugar_mars_slider = widgets.FloatSlider(value=0.3, min=0, max=1, step=0.01, description='Cukier w Mars [kg]')
oil_mars_slider = widgets.FloatSlider(value=0.05, min=0, max=1, step=0.01, description='Olej w Mars [kg]')

choco_snickers_slider = widgets.FloatSlider(value=0.4, min=0, max=1, step=0.01, description='Czekolada w Snickers [kg]')
nuts_snickers_slider = widgets.FloatSlider(value=0.2, min=0, max=1, step=0.01, description='Orzechy w Snickers [kg]')
caramel_snickers_slider = widgets.FloatSlider(value=0.2, min=0, max=1, step=0.01, description='Karmel w Snickers [kg]')
oil_snickers_slider = widgets.FloatSlider(value=0.05, min=0, max=1, step=0.01, description='Olej w Snickers [kg]')

# Wyświetlanie widżetów i uruchomienie optymalizacji
ui = widgets.VBox([
    price_mars_slider, price_snickers_slider,
    max_chocolate_slider, max_caramel_slider, max_sugar_slider, max_oil_slider, max_nuts_slider,
    choco_mars_slider, caramel_mars_slider, sugar_mars_slider, oil_mars_slider,
    choco_snickers_slider, nuts_snickers_slider, caramel_snickers_slider, oil_snickers_slider
])

output = widgets.interactive_output(
    optimize_production,
    {
        'price_mars': price_mars_slider,
        'price_snickers': price_snickers_slider,
        'max_chocolate': max_chocolate_slider,
        'max_caramel': max_caramel_slider,
        'max_sugar': max_sugar_slider,
        'max_oil': max_oil_slider,
        'max_nuts': max_nuts_slider,
        'choco_mars': choco_mars_slider,
        'caramel_mars': caramel_mars_slider,
        'sugar_mars': sugar_mars_slider,
        'oil_mars': oil_mars_slider,
        'choco_snickers': choco_snickers_slider,
        'nuts_snickers': nuts_snickers_slider,
        'caramel_snickers': caramel_snickers_slider,
        'oil_snickers': oil_snickers_slider
    }
)

display(ui, output)
