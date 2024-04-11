from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


menu_items = sa.Table('menu_items', db.metadata, sa.Column('item_id', sa.Integer, sa.ForeignKey('item.id'), primary_key=True), sa.Column('menu_id', sa.Integer, sa.ForeignKey('menu.id'), primary_key=True))

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    account_type: so.Mapped[Optional[str]] = so.mapped_column(
        sa.String(64), index=True, default="viewer"
    )
    last_seen: so.Mapped[Optional[datetime]] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"
    def __repr__(self):
        return "<User {}>".format(self.username)

class Menu(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(140), index=True, unique=True)
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc)
    )
    #items = so.WriteOnlyMapped['Item'] = so.relationship(back_populates='menu')
    items = so.relationship('Item', secondary=menu_items, backref='item')

    def __repr__(self):
        return "<Menu {}>".format(self.name)

class Item(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(140), index=True, unique=True)
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc)
    )
    supply: so.Mapped[int] = so.mapped_column(index=True)

    menu_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Menu.id), index=True)

    menu: so.Mapped[Menu] = so.relationship(back_populates='items')

    def __repr__(self):
        return "<Item {}>".format(self.name)


class Waiter(User):
    # account_type: so.Mapped[Optional[str]] = so.mapped_column(
    #    sa.String(64), index=True, default="waiter"
#)
        
    #class MenuItem(Item):
    ingredients = []
    def sellItem(menuItem):
        return menuItem

        
class Chef(User):
    def createItem(menuItem, ingredients):
        for i in ingredients:
            db.session.add(ingredients[i])
        db.session.commit()
