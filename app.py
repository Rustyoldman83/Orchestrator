app = Flask(__name__)

MCP_BASE_URL = "https://chefskitchenbotmcp.onrender.com"  # Update if your backend URL changes

@app.route("/function_call", methods=["POST"])
def handle_function_call():
    data = request.json
    name = data.get("name")
    arguments = data.get("arguments", {})

    # Route function calls based on function name
    if name == "get_all_nfl_rosters":
        r = requests.get(f"{MCP_BASE_URL}/api/get_all_nfl_rosters")
        return jsonify(r.json())
    # Example: add another function
    # elif name == "get_nfl_schedule":
    #     r = requests.get(f"{MCP_BASE_URL}/api/get_nfl_schedule")
    #     return jsonify(r.json())
    else:
        return jsonify({"error": f"Unknown function: {name}"}), 400

@app.route("/", methods=["GET"])
def home():
    return "ChefBot Orchestrator is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)