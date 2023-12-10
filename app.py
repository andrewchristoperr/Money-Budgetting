from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    # output = run_genetic_algorithm()
    return render_template('index.html')

@app.route('/handle', methods=['POST'])
def handle():
        total = request.form['budget']
        cat1 = request.form['category1']
        cat2 = request.form['category2']
        cat3 = request.form['category3']
        cat4 = request.form['category4']

        p1 = request.form['persen1']
        p2 = request.form['persen2']
        p3 = request.form['persen3']
        p4 = request.form['persen4']
  
        BUDGET_CATEGORIES = []
        Food = [['Bread', int(20), 4], ['Fruits', int(15), 3], ['Vegetables', int(10), 5], ['Potato', int(14), 3], ['Meat', int(24), 6], ['Wagyu', int(30), 20], ['Pizza', int(15), 8],['Odeng', int(12), 6], ['Spaghetti', int(25), 12], ['Salad', int(12), 10], ['Rice', int(3), 1], ['Salted Egg', int(18), 15], ['Chips', int(5), 2], ['Noodles', int(12), 8], ['Meatball', int(13), 6], ['Panini', int(20), 10], ['Soto', int(15), 12], ['Nasi Uduk', int(10), 10], ['Omurice', int(25), 15], ['Wonton', int(13), 5]]
        Utilities = [['Rent', int(50), 60], ['Electricity', int(25), 20], ['Water', int(10), 10], ['Gas', int(7), 15], ['Internet', int(8), 20], ['Health Checkup', int(30), 20], ['Treatment', int(35), 10],['Frozen Food', int(10), 4], ['Skincare', int(20), 15], ['Makeup', int(15), 5], ['Phone Bill', int(10), 10], ['Battery', int(5), 3], ['Security', int(25), 15], ['Water Heater', int(15), 6], ['Woods', int(10), 2], ['Power Bank', int(4), 3], ['Tissue', int(2), 5], ['Gadget', int(150), 200], ['Toys', int(10), 2], ['Employee Salary', int(20), 25]]
        Entertaiment = [['Traveling', int(100), 50], ['Hiking', int(25), 15], ['Swimming', int(10), 8], ['Netflix', int(30), 15], ['Gym', int(10), 4], ['Fishing', int(15), 3], ['Photobooth', int(20), 15],['Video Games', int(8), 4], ['Books', int(25), 20], ['Mukbang', int(50), 30], ['Amusement Park', int(70), 45], ['Cinema', int(25), 15], ['Midnight Drive', int(15), 10], ['Shopping', int(40), 28], ['Ice Skating', int(50), 15], ['Arcade', int(10), 4], ['Going to the beach', int(5), 20], ['Painting', int(12), 6], ['Zombie Run', int(30), 10], ['Board Game', int(8), 8]]
        Asset = [['Credit Card', int(50), 60], ['Gold', int(100), 120], ['E-toll', int(10), 10], ['Investment', int(20), 15], ['House Installment', int(120), 160], ['OVO', int(30), 20], ['Gopay', int(15), 18],['Shopee Pay', int(20), 10], ['Car Installment', int(50), 20], ['Deposito', int(15), 5], ['BCA Stocks', int(30), 50], ['Pasar Uang', int(5), 1], ['BRI Stocks', int(10), 4], ['Dollar', int(20), 30], ['DANA', int(12), 10], ['Insurance', int(40), 30], ['Obligasi', int(30), 10], ['SBN', int(10), 8], ['Jenius', int(15), 6], ['Giftcard', int(6), 4]]
        
        if cat1 == 'Food':
            BUDGET_CATEGORIES.append(Food)
        elif cat1 == 'Asset':
            BUDGET_CATEGORIES.append(Asset)
        elif cat1 == 'Utilities':
            BUDGET_CATEGORIES.append(Utilities)
        elif cat1 == 'Entertainment':
            BUDGET_CATEGORIES.append(Entertaiment)
        
        if cat2 == 'Food':
            BUDGET_CATEGORIES.append(Food)
        elif cat2 == 'Asset':
            BUDGET_CATEGORIES.append(Asset)
        elif cat2 == 'Utilities':
            BUDGET_CATEGORIES.append(Utilities)
        elif cat2 == 'Entertainment':
            BUDGET_CATEGORIES.append(Entertaiment)
        
        if cat3 == 'Food':
            BUDGET_CATEGORIES.append(Food)
        elif cat3 == 'Asset':
            BUDGET_CATEGORIES.append(Asset)
        elif cat3 == 'Utilities':
            BUDGET_CATEGORIES.append(Utilities)
        elif cat3 == 'Entertainment':
            BUDGET_CATEGORIES.append(Entertaiment)
        
        if cat4 == 'Food':
            BUDGET_CATEGORIES.append(Food)
        elif cat4 == 'Asset':
            BUDGET_CATEGORIES.append(Asset)
        elif cat4 == 'Utilities':
            BUDGET_CATEGORIES.append(Utilities)
        elif cat4 == 'Entertainment':
            BUDGET_CATEGORIES.append(Entertaiment)

        categories = []
        
        for i in range (len(BUDGET_CATEGORIES)):
            if BUDGET_CATEGORIES[i] == Food:
                categories.append("Food")
            elif BUDGET_CATEGORIES[i] == Utilities:
                categories.append("Utilities")
            elif BUDGET_CATEGORIES[i] == Entertaiment:
                categories.append("Entertainment")
            elif BUDGET_CATEGORIES[i] == Asset:
                categories.append("Asset")
        cat = categories

        # budget = BUDGET_CATEGORIES
        BUDGET_LIMIT = int(total)
        # categoryLimit = [0.2*BUDGET_LIMIT, 0.2*BUDGET_LIMIT, 0.1*BUDGET_LIMIT, 0.2*BUDGET_LIMIT]
        categoryLimit = []
        categoryLimit.append(int(p1)/100 * BUDGET_LIMIT)
        categoryLimit.append(int(p2)/100 * BUDGET_LIMIT)
        categoryLimit.append(int(p3)/100 * BUDGET_LIMIT)
        categoryLimit.append(int(p4)/100 * BUDGET_LIMIT)

        # output2 = categoryLimit
        FitnessScore = []
        # TotalItems = len(Food)+len(Rent)+len(Entertaiment)
        TotalItems = 0
        for i in range(len(BUDGET_CATEGORIES)):
            temp = len(BUDGET_CATEGORIES[i])
            TotalItems = TotalItems + temp

        # Genetic Algorithm Parameters
        POPULATION_SIZE = 10
        MUTATION_RATE = 0.01
        GENERATIONS = 1

        # Function to calculate fitness 1 individu
        def calculate_fitness(individu):
            total_score = 0
            totalHarga = 0
            for i in range(len(individu)):
                for j in range(len(individu[i])):
                    temp = individu[i][j][2]
                    totalHarga = totalHarga + individu[i][j][1]
                    total_score = total_score + temp  
            fitnessScore = (BUDGET_LIMIT - totalHarga) + total_score
            return fitnessScore

        def create_initial_population():
            population = []
            for _ in range(POPULATION_SIZE):
                individu = []
                for i in range(len(BUDGET_CATEGORIES)):
                    totalPerCat = 0
                    itemPerCat = []
                    while totalPerCat < categoryLimit[i]:
                        temp = random.choice(BUDGET_CATEGORIES[i])
                        # if temp not in itemPerCat:
                        if totalPerCat + temp[1] > categoryLimit[i]:
                            break
                        itemPerCat.append(temp)
                        totalPerCat+=temp[1] 
                    individu.append(itemPerCat)
                population.append(individu)
            return population

        # Function to perform mutation on an individual
        def mutate(individual):
            index = random.randint(0, len(BUDGET_CATEGORIES)-1)
            if individual[index]:
                indexItem = random.randint(0, len(individual[index])-1)
                if random.random() < MUTATION_RATE :
                    newItem = random.choice(BUDGET_CATEGORIES[index])
                    individual[index][indexItem] = newItem
            
            return individual

        # Function to perform crossover between two individuals
        def crossover(parent1, parent2):
            crossover_point = random.randint(1, len(BUDGET_CATEGORIES) - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:] 
            return child

        # Function to select parents based on tournament selection
        def select_parents(population):
            tournament_size = int(POPULATION_SIZE * 0.2)
            parents = []
            for _ in range(2):
                tournament = random.sample(population, tournament_size)
                parent = max(tournament, key=calculate_fitness)
                parents.append(parent)
            return parents

        # Function to calculate fitness scores for the population
        def calculate_population_fitness(population):
            fitness_scores = [calculate_fitness(individual) for individual in population]
            return fitness_scores

        # Genetic Algorithm
        def run_genetic_algorithm():
            generations = []
            for i in range(1, GENERATIONS + 1):
                population = create_initial_population()
                new_population = []
                for _ in range(POPULATION_SIZE // 2):
                    parent1, parent2 = select_parents(population)
                    child1 = crossover(parent1, parent2)
                    child2 = crossover(parent2, parent1)
                    child1 = mutate(child1)
                    child2 = mutate(child2)
                    new_population.extend([child1, child2])
                population = new_population
                generations.append(i)
            best_individual = max(population, key=calculate_fitness)
            return best_individual
        
        list = run_genetic_algorithm()
        budget_cat = BUDGET_CATEGORIES
    
        # Function to output fitness scores for each individual in the population
        def output_fitness_scores(generations, population):
            fitness_scores = calculate_population_fitness(population)
            for generation, score in zip(generations,fitness_scores):
                FitnessScore.append(score)
                print(f"Generation  {generation}: Fitness Score = {score}")
            fittest_score = max(FitnessScore)
            print("Fittest Score: ", fittest_score)
            best_individual = max(population, key=calculate_fitness)
            for i in range (len(BUDGET_CATEGORIES)):
                if BUDGET_CATEGORIES[i] == Food:
                    print("Food")
                elif BUDGET_CATEGORIES[i] == Utilities:
                    print("Utilities")
                elif BUDGET_CATEGORIES[i] == Entertaiment:
                    print("Entertainment")
                elif BUDGET_CATEGORIES[i] == Asset:
                    print("Asset")
                for j in range(len(best_individual[i])):
                        print(best_individual[i][j][0], "$", best_individual[i][j][1],best_individual[i][j][2])
                print("")
            
        category = categoryLimit
        cat1 = cat1
        cat2=cat2
        cat3=cat3
        cat4=cat4
        return render_template('result.html', output=list, len=len(list), budget_cat = budget_cat, cat=cat)
    
if __name__ == '__main__':
    app.run(debug=True)
