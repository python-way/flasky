from . import db

class UserRole(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), unique=True, nullable=False)

class UserAccount(db.Model):
    __tablename__ = 'users_accounts'
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    
    # Nullable text fileds
    city  = db.Column(db.String(100),   nullable=True)
    phone = db.Column(db.String(15),    nullable=True)
    street  = db.Column(db.String(100), nullable=True)

    # Timestamp with database-side current timestamp default
    created_at = db.Column(
            db.DateTime,
            nullable=False,
            server_default=db.func.current_timestamp()
        )

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

class Trainer(db.Model):
    __tablename__ = 'trainers'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), unique=True, nullable=False)

    user_id = db.Column(
            db.Integer, 
            db.ForeignKey('users_accounts.id', ondelete='CASCADE'), 
            nullable=False
        )
    

class Receptionist(db.Model):
    __tablename__ = 'receptionists'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), unique=True, nullable=False)

    user_id = db.Column(
            db.Integer, 
            db.ForeignKey('users_accounts.id', ondelete='CASCADE'), 
            nullable=False
        )

class Equipment(db.Model):
    __tablename__ = 'equipments'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(125), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Exercise(db.Model):
    __tablename__ = 'exercises'
    # Composite Primary Key setup
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), primary_key=True)

    name = db.Column(db.String(125), nullable=False)

    equipment_id = db.Column(db.Integer, db.ForeignKey('equipments.id'), nullable=True)
    description = db.Column(db.Text, nullable=True)

class WorkoutPlan(db.Model):
    __tablename__ = 'workout_plans'
    # Composite Primary Key setup
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), primary_key=True)

    name = db.Column(db.String(125), nullable=False)

    description = db.Column(db.Text, nullable=True)

class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), nullable=False)

    receptionist_id = db.Column(db.Integer, db.ForeignKey('receptionists.id'), nullable=False)

    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), nullable=True)
    workout_plan_id = db.Column(db.Integer, nullable=True)


    __table_args__ = (
        db.ForeignKeyConstraint(
            ['workout_plan_id', 'trainer_id'],
            ['workout_plans.id', 'workout_plans.trainer_id']
        ),
        db.Index('idx_member_plan_trainer', 'workout_plan_id', 'trainer_id'),
    )

class WorkoutPlanExercise(db.Model):
    __tablename__ = 'workout_plan_exercises'
    
    workout_plan_id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, primary_key=True)

    # Composite Foreign Keys targeting composite parents
    __table_args__ = (
        db.ForeignKeyConstraint(
            ['workout_plan_id', 'trainer_id'],
            ['workout_plans.id', 'workout_plans.trainer_id']
        ),
        db.ForeignKeyConstraint(
            ['exercise_id', 'trainer_id'],
            ['exercises.id', 'exercises.trainer_id']
        ),
    )

class ProgressReport(db.Model):
    __tablename__ = 'progress_reports'
    
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), primary_key=True)
   
    date = db.Column(
        db.Date, 
        nullable=True, 
        server_default=db.func.current_date()
    )
    progress_notes = db.Column(db.Text, nullable=True)


    date = db.Column(db.Date, nullable=False)
    progress_notes = db.Column(db.Text, nullable=True)
