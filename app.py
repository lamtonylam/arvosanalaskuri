from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate_required_points(minimum_points, maximum_points):
    points = {}
    step = (maximum_points - minimum_points) / 4
    
    points[1] = minimum_points
    points[2] = minimum_points + step
    points[3] = minimum_points + 2 * step
    points[4] = minimum_points + 3 * step
    points[5] = maximum_points
    
    return points

def calculate_grade(minimum_points, maximum_points, user_points):
    if user_points < minimum_points:
        return 0
    elif user_points >= maximum_points:
        return 5
    else:
        grade = 1 + 4 * (user_points - minimum_points) / (
            maximum_points - minimum_points
        )
        return math.floor(grade)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    required_points = None
    
    if request.method == 'POST':
        try:
            minimum_points = float(request.form.get('minimum_points', 0))
            maximum_points = float(request.form.get('maximum_points', 0))
            
            # calculate required points for each grade
            required_points = calculate_required_points(minimum_points, maximum_points)
            
            # Cclculate user grade if user points were provided
            if 'user_points' in request.form and request.form['user_points']:
                user_points = float(request.form['user_points'])
                grade = calculate_grade(minimum_points, maximum_points, user_points)
                result = {
                    'user_points': user_points,
                    'grade': grade
                }
                
        except ValueError:
            # handle invalid input
            error = "Please enter valid numbers"
            return render_template('index.html', error=error)
    
    return render_template('index.html', result=result, required_points=required_points)

if __name__ == '__main__':
    app.run(debug=True)