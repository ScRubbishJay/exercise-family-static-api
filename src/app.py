from flask import Flask, jsonify, request
from datastructures import FamilyStructure

app = Flask(__name__)
family = FamilyStructure("Smith")
 
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify({'family': family.get_all_members()})

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = family.get_member(id)
    if member:
        return jsonify(member)
    else:
        return jsonify({'error': 'Member not found'}), 404

@app.route('/member', methods=['POST'])
def add_member():
    data = request.json
    if data:
        member_id = family.add_member(data)
        return jsonify({'member_id': member_id}), 201
    else:
        return jsonify({'error': 'Invalid data'}), 400

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    result = family.delete_member(id)
    if result['done']:
        return jsonify(result)
    else:
        return jsonify({'error': 'Member not found'}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
