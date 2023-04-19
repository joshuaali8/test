from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import CetlUser, Lecturer, User
from . import lecturer_blueprint
from . import cetl_blueprint

chat_blueprint = Blueprint('chat', __name__)

@chat_blueprint.route("/chat", methods=['POST'] )
def add_message():
    sender_id = request.json['sender_id']
    recipient_id = request.json['recipient_id']
    message = request.json['message']

    msg = Message(sender_id=sender_id, recipient_id=recipient_id, message=message)
    db.session.add(msg)
    db.session.commit()

    socketio.emit('message', {'sender_id': sender_id, 'recipient_id': recipient_id, 'message': message}, broadcast=True)

    return '', 200

@chat_blueprint.route('/chat/<int:sender_id>/<int:recipient_id>', methods=['GET'])
def get_messages(sender_id, recipient_id):
    # query the messages table for messages between the sender and recipient
    messages = Message.query.filter(
        (Message.sender_id == sender_id and Message.recipient_id == recipient_id) |
        (Message.sender_id == recipient_id and Message.recipient_id == sender_id)
    ).order_by(Message.timestamp.asc()).all()

    # serialize the messages to JSON format
    messages_json = [message.to_dict() for message in messages]

    return jsonify(messages_json)






